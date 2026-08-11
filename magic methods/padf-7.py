class cart:
    def __init__(self,item,price,qty):
        self.item=item
        self.price=price
        self.qty=qty
    def final(self):
        return self.price*self.qty
    def __str__(self):
        return f"item name:{self.item}\nitem prioce:{self.price}\nitem quantity:{self.qty}"
    def __add__(self,other):
        return self.final()+other.final()
    def __mod__(self,other):
        return self.final()%other
a=cart("pen",20,5)
b=cart("shirt",300,4)
print(a)
print("-"*13)
print(b)
print("-"*13)
print("comparition details:")
print("add final amount:",a+b)
print("mod operation:",a%30)

