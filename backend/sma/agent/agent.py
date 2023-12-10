import json
import random


from backend.sma.body.body import Body


class Agent:
    def __init__(self,type="",line=""):
        self.uuid=random.randint(10000000,100000000)
        self.body=Body(line)
        self.perceptionsItem=[]
        self.perceptionsAgent=[]
        self.type=type

    def doDecision(self):
        pass


    def to_json(self):
        json.dumps(self.__dict__)