import random
import math
from backend.sma.body.body import Body
from backend.sma.environment.vehicle import Vehicle
from backend.helper.routing import get_route
from backend.sma.agent.agent import Agent


class Passager(Agent):
    def __init__(self):
        super.__init__(type="Rider",origine=[], destination=[],vehicle=None)
        self.initialPosition = [random.uniform(4.5, 5.1), random.uniform(45.4, 46)]
        self.currentPosition = self.initialPosition
        self.destination = [random.uniform(4.5, 5.1), random.uniform(45.4, 46)]


    def actions(self):
        if self.stats != "WAITING" and self.stats != "REQUEST SEND":
            distanceToDestination = self.distanceToDestination()
        if distanceToDestination < 2:
            self.body.path = get_route(self.currentPosition, self.destination)
        else:
            self.perceptionsAgent.sort(key=lambda x: x.distance_to, reverse=False)
            if len(self.perceptionsAgent) > 0:
                driver = [i for i in self.perceptionsAgent if
                          i.vehicle is not None and len(i.vehicle.passager) < i.vehicle.capacity]

                





    def distanceToDestination(self):

        lat1, lon1 = self.currentPosition
        lat2, lon2 = self.destination
        R = 6371.0
        lat1, lon1 = math.radians(lat1), math.radians(lon1)
        lat2, lon2 = math.radians(lat2), math.radians(lon2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c

        return distance

