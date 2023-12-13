import random

from helper.math import lerp
from sma.body.fustrum import Fustrum
from time_aware_polyline import decode_time_aware_polyline
from datetime import datetime, timedelta
from helper.routing import get_route

def date_to_datetime(dateStr):
    try:
        # 2023-06-14T15:39:20
        date_time_obj = datetime.strptime(dateStr[:19], "%Y-%m-%dT%H:%M:%S")

    except Exception as e:
        print('erreur ', e, type(dateStr), dateStr[:19])

    return date_time_obj

class Body:
    def __init__(self,origine,destination,vehicle):
        self.fustrum = Fustrum()
        self.uuid=random.randint(10000000,100000000)

        self.path= get_route(origine,destination)
        if len(self.path)>0:
            self.pos = self.path[0]
        else:
            self.pos=[random.randint(0,10000),random.randint(10000,0)]

        self.visible=True
        self.vehicle=vehicle
        self.mass=10
        self.vel = 0
        self.mailbox=[]



    def update(self,tic):
        if self.vel==1:
            if len(self.path)>1:
                while self.path[1][2]<tic :
                    self.pos=self.path[1]
                    self.path=self.path[1:]



                if self.path[1][2]<tic:
                    self.pos=self.path[1]
                    self.path=self.path[1:]
                else:

                    tic_ts = tic
                    iv=self.path[0][2]
                    ov=self.path[1][2]

                    self.pos = [lerp(tic_ts,iv,ov,self.path[0][0],self.path[1][0]),
                                lerp(tic_ts,iv,ov,self.path[0][1],self.path[1][1])]


            else:
                self.pos = [0,0]

