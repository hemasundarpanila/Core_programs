class product:
    basetax=5
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def final(self):
        total=self.price+(self.price*product.basetax/100)
        return total
    @classmethod
    def change(cls,new):
        cls.basetax=new
    @staticmethod
    def check(Aa):
        return Aa>0
    def display(self):
        print("customer name:",self.name)
        print("product price:",self.price)
        print("final price:",self.final())
        print("_"*13)
a=product("shiva",1000)
b=product("nani",2000)
a.display()
b.display()
product.change(15)
print("after update the tax:")
a.display()
b.display()




        
