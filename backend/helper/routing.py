from config import OPEN_ROUTE_SERVICE_KEY
from helper.math import distance
from openrouteservice import Client, convert
from openrouteservice.directions import directions


def get_route(origine: list, destination: list):
    client = Client(key=OPEN_ROUTE_SERVICE_KEY)
    route = directions(
        client,
        ([origine[1], origine[0]], [destination[1], destination[0]]),
        profile="driving-car",
        preference="fastest",
    )

    path = convert.decode_polyline(route["routes"][0]["geometry"])

    path2 = [[path["coordinates"][0][1], path["coordinates"][0][0], 0]]
    tps = 0
    for i in range(1, len(path["coordinates"])):
        tps += (
            distance(
                [path["coordinates"][i - 1][1], path["coordinates"][i - 1][0]],
                [path["coordinates"][i][1], path["coordinates"][i][0]],
            )
            * 1000
            / 3.6
        )
        path2.append([path["coordinates"][i][1], path["coordinates"][i][0], tps])

    return path2
