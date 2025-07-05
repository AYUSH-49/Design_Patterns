from AbstractFactory.uiFactory import IosButton
from Factory import Factory

class IosButtonFactory(Factory):
    """Factory for creating Android buttons."""
    def create(self):
        return IosButton()

