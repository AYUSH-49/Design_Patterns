import copy
from Monster import Monster

class Gobline(Monster):
    def __init__(self,health=100):
        self.health = health
        

    def attack(self):
        print("Gobline attacks with a dagger!", self.health)

    def clone(self):
        return copy.deepcopy(self)