from body import Body
from helper.route import Route


class BodyTAD(Body):
    def __init__(self, origine, destination, vehicle):
        super().__init__(origine, destination, vehicle)
        # self.path = Route(origine,destination)
        self.path = None
