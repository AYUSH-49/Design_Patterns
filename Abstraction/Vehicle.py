from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,num_of_tires):
        self.num_of_tires = num_of_tires

    #@abstractmethod
    def start(self):
        pass

