from Players_factory import Players_factory
from Knight import Knight


class Knight_Factory(Players_factory):

    def Create_Player(self):

        return Knight().attack()