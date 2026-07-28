class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposite(self,add):
        k=self.balance+add
        print(k)
    @classmethod
    def change_name(cls,name):
        cls.bank_name=name
    @staticmethod
    def valid_amount(amount):
        return amount>0
a=BankAccount("shiva",30000)
b=BankAccount("nani",50000)
print(a.holder,a.balance)
print(b.holder,b.balance)
a.deposite(3000)
b.deposite(5000)
BankAccount.change_name("andhra bank")
print(a.bank_name)
print(BankAccount.valid_amount(20000))
        
