from helper.routing import get_route


class Route:
    def __init__(self, origin: list, destination: list):
        self.origin = origin
        self.destination = destination
        self.path = get_route(self.origin, self.destination)
