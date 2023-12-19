import json
import random


from backend.sma.body.body import Body
from backend.sma.environment.messages import Message


class Agent:
    def __init__(self,type="",origine=[], destination=[],vehicle=None):
        self.uuid=random.randint(10000000,100000000)
        self.body=Body(origine,destination,vehicle)
        self.perceptionsItem=[]
        self.perceptionsAgent=[]
        self.type=type
        self.stats="WAITING"
        

    def doDecision(self):
        self.perceptionsAgent.sort(key=lambda x: x.distance_to, reverse=False)

        if self.type=="Rider":
            if len(self.perceptionsAgent)>0:
                driver = [i for i in self.perceptionsAgent if i.vehicle is not None and len(i.vehicle.passager)<i.vehicle.capacity]
                if self.stats=="WAITING":
                    if len(driver)>0:
                        msg=Message()
                        msg.from_to = self
                        msg.msg="Request carpool"
                        driver[0].mailbox.append(msg)
                        self.stats="REQUEST SEND"
                if self.stats=="REQUEST SEND":
                    if len(driver)>0:
                        if len(self.body.mailbox)>0:
                            msg=self.body.mailbox[0]
                            if msg.msg=="REQUEST ACCEPTED":
                                if driver[0].distance_to <20:
                                    self.body.visible=False
                                    msg.from_to.type="CARPOOL"
                                    msg.from_to.body.vehicle.passager.append(self.uuid)
                                    self.stats = "ON RIDE"
        if self.type=="Driver":
            self.body.vel=1
            if len(self.perceptionsAgent):
                rider = [i for i in self.perceptionsAgent if i.vehicle is None]
                if len(rider)>0:
                    if len(self.body.mailbox)>0:
                        for m in self.body.mailbox:
                            if self.body.vehicle.capacity>len(self.body.vehicle.passager):
                                if m.msg=="Request carpool":
                                    msg=Message()
                                    msg.from_to = self
                                    msg.msg="REQUEST ACCEPTED"
                                    m.from_to.body.mailbox.append(msg)
                                    self.body.mailbox.remove(m)


                                














    def to_json(self):
        json.dumps(self.__dict__)