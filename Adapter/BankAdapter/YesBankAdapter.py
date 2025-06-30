from Adapter.AbstractAdapter import AbstractAdapter
from Adapter.Bank.YesBank import YesBank


class YesBankAdapter(AbstractAdapter):
    def __init__(self):
        self.bank=YesBank()

    def CheckBalance(self):
        return self.bank.balance()
