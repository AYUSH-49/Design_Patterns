from abc import ABC,abstractmethod
from AndroidBottonFactory import AndroidButtonFactory
from AndroidCheckBoxFactory import AndroidCheckBoxFactory

class AbstractAndroidFactory(ABC):

    def create_button():

        return AndroidButtonFactory()
    
    def create_checkbox():
        
        return AndroidCheckBoxFactory()
