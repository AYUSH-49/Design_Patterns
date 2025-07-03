from Players_factory import Players_factory
from Mage_V2 import Mage_V2

class Mage_Factory(Players_factory):
    def Create_Player(self):

        return Mage_V2().attack()
        