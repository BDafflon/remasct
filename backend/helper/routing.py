import openrouteservice
from openrouteservice.directions import directions
from backend.helper.math import distance


def get_route(origine, destination):
    client = openrouteservice.Client(key = "5b3ce3597851110001cf62483c423a78571445a686606bc1f7f2c45c")
    route = directions(client, ([origine[1],origine[0]],
                                    [destination[1],destination[0]]),
                           profile='driving-car', preference="fastest")
     
    path = openrouteservice.convert.decode_polyline(route['routes'][0]['geometry'])
    
    path2 = [[path["coordinates"][0][1],path["coordinates"][0][0],0]]
    tps=0
    for i in range(1,len(path["coordinates"])):
        tps+=distance([path["coordinates"][i-1][1],path["coordinates"][i-1][0]],[path["coordinates"][i][1],path["coordinates"][i][0]])*1000/3.6
        path2.append([path["coordinates"][i][1],path["coordinates"][i][0],tps])
    
 
    return path2