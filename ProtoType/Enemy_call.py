from Orc import Orc
from Gobline import Gobline
from Zombies import Zombies


class Enemy_call:
    def __init__(self, TypeofEnemy, NoOfClones):
        self.TypeofEnemy = TypeofEnemy
        self.NoOfClones = NoOfClones
    
    def create_enemy(self):
        if self.TypeofEnemy == "orc":
            orignal_orc = Orc()
            clone= [orignal_orc.clone() for x in range(self.NoOfClones)]
            enemies= [orignal_orc] + clone
            for i  in enemies:
                i.attack()
            return enemies
        elif self.TypeofEnemy == "gobline":
            orignal_gobline = Gobline()
            clone= [orignal_gobline.clone() for x in range(self.NoOfClones)]
            enemies= [orignal_gobline] + clone
            for i  in enemies:
                i.attack()  
            return enemies
        elif self.TypeofEnemy == "zombie":
            orignal_zombie = Zombies()
            clone= [orignal_zombie.clone() for x in range(self.NoOfClones)]
            enemies= [orignal_zombie] + clone
            for i  in enemies:
                i.attack()  
            return enemies
        else:
            print("Invalid enemy type")
            return None
            
        
        

        