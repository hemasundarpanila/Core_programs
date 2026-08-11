    # class Box:

    #     def __init__(self, value):
    #         self.value = value

    #     def __add__(self, other):
    #         return self.value + other.value
    # b1 = Box(10)
    # b2 = Box(20)
    # print(b1+b2)




# class shopping:
#     def __init__(self):
#         self.cart=[]
#     def __add__(self,other):
#         self.cart.append(other)
#         return self
# c1=shopping()
# c2=shopping()
# c1+"apple"+"banana"
# c2+"orange"
# print(c1.cart)
# print(c2.cart)
# print(d.cart)
# d=c1.cart+c2.cart
#print(d)

# c1 = Shopping()
# c2 = Shopping()

# c1 + "Apple"
# c1 + "Banana"

# c2 + "Orange"
# c2 + "Mango"

# c3 = c1 + c2

# print(c3.cart)

class Shopping:
    
    def __init__(self):
        self.cart = []

    def __add__(self, other):
        self.cart.append(other)
        return self
c1=Shopping()
c2=Shopping()
c1+"apple"+"banana"
c2+"orange"
c3=c1.cart+c2.cart
print(c3)
