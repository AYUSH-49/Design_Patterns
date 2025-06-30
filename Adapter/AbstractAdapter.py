from abc import ABC


class AbstractAdapter(ABC):

    def CheckBalance(self):
        pass

    def AddMoney(self):
        pass


    def SendMoney(self):
        pass