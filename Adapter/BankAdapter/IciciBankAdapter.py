from Adapter.AbstractAdapter import AbstractAdapter
from Adapter.Bank.IciciBank import IciciBank


class IciciBankAdapter(AbstractAdapter):
    def __init__(self):
        self.bank=IciciBank()

    def CheckBalance(self):
        return self.bank.bal()
