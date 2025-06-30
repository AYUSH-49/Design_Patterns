from AbstractFactory.uiFactory.IosButton import IosButton

class IosButtonFactory(Factory):
    """Factory for creating Android buttons."""
    def create(self):
        return IosButton()

