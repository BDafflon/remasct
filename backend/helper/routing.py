import openrouteservice
from openrouteservice.directions import directions
from helper.math import distance

def get_route(origine, destination):
    client = openrouteservice.Client(key = "5b3ce3597851110001cf6248d5f91ac8b85043b3ba1584a754423c88")
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