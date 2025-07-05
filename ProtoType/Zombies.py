import copy
from Monster import Monster

class Zombies(Monster):
    def __init__(self,health=100):
        self.health = health
        

    def attack(self):
        print("Zombie attacks with a bite!", self.health)

    def clone(self):
        return copy.deepcopy(self)