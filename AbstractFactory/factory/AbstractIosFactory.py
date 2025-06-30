from abc import ABC,abstractmethod

import IosButtonFactory
import IosCheckBoxFactory


class AbstractAndroidFactory(ABC):

    def create_Button():

        return IosButtonFactory()
    
    def create_checkbox():
        
        return IosCheckBoxFactory()
