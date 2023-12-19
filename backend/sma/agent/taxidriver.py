from backend.sma.agent.agent import Agent
from backend.sma.environment.vehicle import Vehicle
from backend.sma.environment.messages import Message


class TaxiDriver(Agent):
    def __init__(self):
        super().__init__(type="Driver", vehicle=Vehicle(capacity=1))

    def doDecision(self):
        self.body.vel = 1
        if len(self.body.vehicle.passager) >= self.body.vehicle.capacity:
            msg = Message()
            msg.from_to = self
            msg.msg = "IN SERVICE"
            msg.msg_to = CENTRALE
            msg.msg_to.body.mailbox.append(msg)

        if len(self.perceptionsAgent):
            rider = [i for i in self.perceptionsAgent if i.vehicle is None]
            if len(rider) > 0:
                if len(self.body.mailbox) > 0:
                    for m in self.body.mailbox:
                        if self.body.vehicle.capacity > len(self.body.vehicle.passager):
                            if m.msg == "Request carpool":
                                msg = Message()
                                msg.from_to = self
                                msg.msg = "REQUEST ACCEPTED"
                                m.from_to.body.mailbox.append(msg)
                                self.body.mailbox.remove(m)

