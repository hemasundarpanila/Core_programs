class Tax:
    base_tax=500
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def final(self):
        return self.price+self.base_tax
    @classmethod
    def change_tax(cls,tax_rate):
        cls.base_tax=tax_rate
    @staticmethod
    def check():
        return 10000>=price
    def display(self):
        print("person name:",self.name)
        print("person price:",self.price)
        print("adding tax:",self.final())
        print("_"*15)
a=Tax("shiva",10000)
b=Tax("nani",20000)
Tax.change_tax(1000)
a.display()
b.display()

