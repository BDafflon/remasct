
import json
from datetime import datetime, timedelta
import copy
import time
from sma.agent.agent import Agent
from sma.item.vehicle import Vehicle
from json import JSONEncoder


def date_to_datetime(dateStr):
    try:
        # 2023-06-14T15:39:20
        date_time_obj = datetime.strptime(dateStr[:19], "%Y-%m-%dT%H:%M:%S")

    except Exception as e:
        print('erreur ', e, type(dateStr), dateStr[:19])

    return date_time_obj


class Environment:
    def __init__(self):
        self.width=500
        self.height=500
        self.items=[]
        v = Vehicle()
        self.agents=[Agent(type="Driver",vehicle=v,origine=[45.7794863625781, 4.833639417972437], destination=[45.10143228767492, 5.877751348599213]),
                     Agent(type="Rider",origine=[45.77944162307949, 4.841086087484752], destination=[45.10143228767492, 5.877751348599213])
                     ]
        
        print(self.agents[1].body.path)
        self.tic_min=min([i.body.path[0][2] for i in self.agents])
        self.tic=self.tic_min
        self.tic_max=max([i.body.path[len(i.body.path)-1][2] for i in self.agents])

    def computePerception(self,agent):
        perceptions = []
        for a in self.agents:
            if a.uuid != agent.uuid:
                dist,inside = agent.body.fustrum.inside(a.body,agent.body)
                if inside:
                    perception = a.body
                    perception.distance_to=dist
                    perceptions.append(perception)
        agent.perceptionsAgent=perceptions[:]
        perceptions=[]
        for i in self.items:
            if agent.body.fustrum.inside(i,agent.body):
                perceptions.append(i)
        agent.perceptionsItem=perceptions[:]


    def computeDecision(self,agent):
        agent.doDecision()

    def applyDecision(self,agent):
        agent.body.update(self.tic)
        
    def run(self,tic):
        self.tic+=tic
        if self.tic > self.tic_max:
            self.tic=self.tic_min

        for a in self.agents:
            self.computePerception(a)
            self.computeDecision(a)

        for a in self.agents:
            self.applyDecision(a)



