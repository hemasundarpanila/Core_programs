class loan:
    common_interest=10
    def __init__(self,name,principal):
        self.name=name
        self.principal=principal
    def add(self):
        total_pay=self.principal+(self.principal*loan.common_interest/100)
        return total_pay
    @classmethod
    def change(cls,new):
        cls.common_interest=new
    @staticmethod
    def check(AA):
        return AA>5000
    def display(self):
        print("customer name:",self.name)
        print("customer principal:",self.principal)
        print("total amount:",self.add())
        print("check:",loan.check(self.principal))
        print("-"*13)
        pass
a=loan("shiva",20000)
b=loan("nani",30000)
a.display()
b.display()
loan.change(20)
print("after change the principal:")
a.display()
b.display()
