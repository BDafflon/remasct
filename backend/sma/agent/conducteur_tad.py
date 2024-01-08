from agent import Agent
from body.body_tad import BodyTAD


class conducteurTAD(Agent):
    def __init__(self, depot, type="", origine=..., destination=..., vehicle=None):
        super().__init__(type, origine, destination, vehicle)
        self.body = BodyTAD(origine, destination, vehicle)
        self.depot = depot

    def doDecision(self):
        pass
