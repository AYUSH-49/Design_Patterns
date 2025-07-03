from Computer_Builder import ComputerBuilder
from Computer import Computer

class NormalComputerBuilder(ComputerBuilder):
    def __init__(self,cpu=None, ram=None, storage=0, gpu=None, power_supply=0):
        self.set_cpu(float(input("Enter CPU speed (GHz): ")))
        self.set_ram(int(input("Enter RAM size (GB): ")))
        self.set_storage(int(input("Enter Storage size (GB): ")))
        self.set_gpu(int(input("Enter GPU size (GB): ")))
        self.set_power_supply(int(input("Enter Power Supply wattage (W): ")))

      
    def set_cpu(self, cpu):
        if cpu < 2:
            raise ValueError("CPU must be at least 2 GHz for a Normal computer.")
        self.cpu = cpu
    def set_ram(self, ram):
        if ram<4:
            raise ValueError("RAM must be at least 8 GB for a Normal computer.")    
        self.ram = ram
    
    def set_storage(self, storage):
        if storage<512:
            raise ValueError("Storage must be at least 512 GB for a Normal computer.")
        self.storage = storage

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_power_supply(self, power_supply):
        if power_supply<500:
            raise ValueError("Power supply must be at least 500W for a Normal computer.")
        self.power_supply = power_supply
    
    def built(self):
        return Computer(self)
        
        