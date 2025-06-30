from knight import Knight
from archer import Archer
from mage import Mage
from abc import ABC, abstractmethod


class PlayerFactory(ABC):

    @abstractmethod
    def create_Player(self):
        pass

            
class KnightFactory:
    def create_Player(self):

        return Knight() 
    

class ArcherFactory:
    def create_Player(self):

        return Archer()
    

class MageFactory:
    def create_Player(self):

        return Mage()
        
