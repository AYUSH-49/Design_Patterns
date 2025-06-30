from Adapter.BankAdapter.IciciBankAdapter import IciciBankAdapter
from Adapter.BankAdapter.YesBankAdapter import YesBankAdapter
from Adapter.Phonepe import Phonepe

if __name__ == '__main__':
    b=IciciBankAdapter()
    p= Phonepe(b)
    print(p.checkBalance())
    C=YesBankAdapter()
    P2=Phonepe(C)
    print(P2.checkBalance())