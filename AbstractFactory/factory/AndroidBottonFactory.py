from factory import Factory
from AbstractFactory.uiFactory.AndroidButton import AndroidButton 


class AndroidButtonFactory(Factory):
    """Factory for creating Android buttons."""
    def create(self):
        return AndroidButton()

