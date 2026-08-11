class BankAccount:
    bank="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposite(self,amount):
        self.balance=self.balance+amount
    @classmethod
    def change(cls,new):
        cls.bank=new
    @staticmethod
    def valid(Aa):
        return Aa>0
    def display(self):
        print("holder name:",self.holder)
        print("balance:",self.balance)
        print("validity:",BankAccount.valid(self.balance))
        print("bank name:",BankAccount.bank)
        print("_"*12)
               
a=BankAccount("shiva",10000)
b=BankAccount("nani",20000)
BankAccount.change("Andhra bank")
a.display()
b.display()
a.deposite(2000)
b.deposite(3000)
print("after deposite:")
a.display()
b.display()




            
        
