from Players_factory import Players_factory
from Archer import Archer

class Archer_Factory(Players_factory):
    def Create_Player(self):

        return Archer().attack()