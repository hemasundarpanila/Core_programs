class Bank:

    bank_name = "SBI"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name)
        print(self.balance)
    @classmethod
    def bank(cls):
        print(cls.bank_name)
    @staticmethod
    def minimum_balance():
        print("Minimum Balance = 1000")
a = Bank("Ravi", 5000)
a.display()
Bank.bank()
Bank.minimum_balance()
# k=["shiva","kumar","reddy"]
# l=list(map(lambda x:list(filter(lambda y:y in "AEIOUaeiou",x)),k))
# print(l)