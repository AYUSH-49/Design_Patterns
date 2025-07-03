from GamingComputerBuilder import GamingComputerBuilder
from NormalComputerBuilder import NormalComputerBuilder
class BuilderDirectory:
    def __init__(self,TOB):
        self.TOB = TOB

    def get_builder(self):
        if self.TOB == "Gaming":
            return GamingComputerBuilder()
        
        elif self.TOB == "Normal":
            return NormalComputerBuilder()
        
        else:
            raise ValueError("Unknown type of computer builder requested.")