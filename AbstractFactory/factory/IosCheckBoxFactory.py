from factory import Factory
from AbstractFactory.uiFactory.IosCheckbox import IosCheckbox


class IosCheckBoxFactory(Factory):
    """Factory for creating Android buttons."""
    def create(self):
        return IosCheckbox()

