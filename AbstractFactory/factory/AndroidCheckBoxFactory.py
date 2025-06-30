from factory import Factory
from AbstractFactory.uiFactory.AndroidCheckbox import AndroidCheckbox


class AndroidButtonFactory(Factory):
    """Factory for creating Android buttons."""
    def create(self):
        return AndroidCheckbox()

