from abc import ABC, abstractmethod 

class Abstract_Factory (ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass