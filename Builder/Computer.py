class Computer:
    def __init__(self, builder):# Computer class that takes a builder object
        self.cpu = builder.cpu
        self.ram = builder.ram
        self.storage = builder.storage
        self.gpu = builder.gpu
        self.power_supply = builder.power_supply
        
    
    def set_cpu(self, cpu):
        self.cpu = cpu
    def set_ram(self, ram):
        self.ram = ram
    def set_storage(self, storage):
        self.storage = storage
    def set_gpu(self, gpu):
        self.gpu = gpu
    def set_power_supply(self, power_supply):
        self.power_supply = power_supply
    
    def __str__(self):
        return (f"Computer Specifications:\n"
                f"CPU: {self.cpu} GHz\n"
                f"RAM: {self.ram} GB\n"
                f"Storage: {self.storage} GB\n"
                f"GPU: {self.gpu} GB\n"
                f"Power Supply: {self.power_supply} final")