from backend.helper.math import distance

class Fustrum:
    def __init__(self):
        self.radius=100

    def inside(self,target, parent):
        return distance(target.pos,parent.pos)*1000,distance(target.pos,parent.pos)*1000 < self.radius

