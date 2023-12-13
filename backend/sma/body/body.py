import random

from helper.math import lerp
from sma.body.fustrum import Fustrum
from time_aware_polyline import decode_time_aware_polyline
from datetime import datetime, timedelta


def date_to_datetime(dateStr):
    try:
        # 2023-06-14T15:39:20
        date_time_obj = datetime.strptime(dateStr[:19], "%Y-%m-%dT%H:%M:%S")

    except Exception as e:
        print('erreur ', e, type(dateStr), dateStr[:19])

    return date_time_obj

class Body:
    def __init__(self,line,vehicle):
        self.fustrum = Fustrum()
        self.pos = [4.859506014597364,45.77890591958584]
        self.polyline = line
        self.path=  decode_time_aware_polyline(self.polyline)
        self.visible=True
        self.vehicle=vehicle
        self.mass=10
        self.vel = 10


    def update(self,tic):
        if len(self.path)>1:

            if date_to_datetime(self.path[1][2])<tic:
                self.pos=self.path[1]
                self.path=self.path[1:]
            else:

                tic_ts = datetime.timestamp(tic)
                iv=datetime.timestamp(date_to_datetime(self.path[0][2]))
                ov=datetime.timestamp(date_to_datetime(self.path[1][2]))

                self.pos = [lerp(tic_ts,iv,ov,self.path[0][0],self.path[1][0]),
                            lerp(tic_ts,iv,ov,self.path[0][1],self.path[1][1])]


        else:
            self.pos = [0,0]

