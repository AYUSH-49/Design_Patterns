import copy
from Monster import Monster

class Orc(Monster):
    def __init__(self,health=100):
        self.health = health
        

    def attack(self):
        print("Orc attacks with a club!", self.health)
       


    def clone(self):
        return copy.deepcopy(self)