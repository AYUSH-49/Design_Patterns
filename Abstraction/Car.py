
from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, num_of_tires, color):
        super().__init__(num_of_tires)
        self.color =color
    
    def start(self):
        print("Start")


c = Car(4,"Blue")

c.start()
print(c.num_of_tires)
