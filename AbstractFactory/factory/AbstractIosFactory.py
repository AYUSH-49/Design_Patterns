from Abstract_Factory import Abstract_Factory
from IosButtonFactory import IosButtonFactory
from IosCheckBoxFactory import IosCheckBoxFactory


class AbstractIosFactory(Abstract_Factory):

    def create_Button():
        return IosButtonFactory()
    
    def create_checkbox():        
        return IosCheckBoxFactory()
