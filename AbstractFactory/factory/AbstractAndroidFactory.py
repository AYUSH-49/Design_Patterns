from Abstract_Factory import Abstract_Factory
from AndroidBottonFactory import AndroidButtonFactory
from AndroidCheckBoxFactory import AndroidCheckBoxFactory


class AbstractAndroidFactory(Abstract_Factory):

    def create_button():
        return AndroidButtonFactory()
    
    def create_checkbox():    
        return AndroidCheckBoxFactory()
