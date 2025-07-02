from GamingComputerBuilder import GamingComputerBuilder
from NormalComputerBuilder import NormalComputerBuilder
class BuilderDirectory:
    def __init__(self,TOB):
        self.TOB = TOB

    def get_builder(self):
        if self.TOB == "Gaming":
            cpu=input("Enter CPU speed (GHz): ")
            ram=input("Enter RAM size (GB): ")
            storage=input("Enter Storage size (GB): ")
            gpu=input("Enter GPU size (GB): ")
            power_supply=input("Enter Power Supply wattage (W): ")

            return GamingComputerBuilder(cpu, ram, storage, gpu, power_supply)
        elif self.TOB == "Normal":
            cpu=input("Enter CPU speed (GHz): ")
            ram=input("Enter RAM size (GB): ")
            storage=input("Enter Storage size (GB): ")
            gpu=input("Enter GPU size (GB): ")
            power_supply=input("Enter Power Supply wattage (W): ")
            return NormalComputerBuilder(cpu, ram, storage, gpu, power_supply)
        else:
            raise ValueError("Unknown type of computer builder requested.")