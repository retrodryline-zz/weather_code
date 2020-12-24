#Wasatch Crest above Centerville

40.965312, -111.815057
#closet point is just east of Grandview peak lats[111,161], lons[111,161] #note [112,161] is right near Mountain Green

from math import radians, cos, sin, asin, sqrt 
dist=np.zeros((lats.shape[0],lats.shape[1])) for x in range(lats.shape[1]): for y in range(lats.shape[0]): # convert decimal degrees to radians lat1, long1, lat2, long2 = map(radians, [lats[y,x], lons[y,x], 40.965312, -111.815057]) # haversine formula dlon = long2 - long1 dlat = lat2 - lat1 a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)*2 c = 2 * asin(sqrt(a)) # Radius of earth in kilometers is 6371 dist[y,x] = 6371 c

#give closet point
np.amin(dist), np.where(dist == np.amin(dist))
