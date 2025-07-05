from Knight_Factory import Knight_Factory
from Archer_factory import Archer_Factory
from Mage_factory import Mage_Factory


class Character():
    def __init__(self, Player_Type):
        self.Player_Type = Player_Type
       

    def create_player(self):
        if self.Player_Type == 'knight':
            return Knight_Factory().Create_Player()
        elif self.Player_Type == 'archer':
            return Archer_Factory().Create_Player()
        elif self.Player_Type == 'mage':       
            return Mage_Factory().Create_Player()
        else:
            raise ValueError("Unknown player type: {}".format(self.Player_Type))
        