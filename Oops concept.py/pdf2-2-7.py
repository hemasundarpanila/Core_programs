# class inventory:
#     total_items=0
#     min_stock=5
#     def __init__(self):
#         self.stock={}
#     def add(self,item,qty):
#         self.stock[item]=qty
#         inventory.total_items+=qty
#     def remove(self,item,qty):
#         self.stock[item]=self.stock[item]-qty
#     @classmethod
#     def update(cls,new):
#         cls.min_stock=new
#     @staticmethod
#     def check(qtyt):
#         return qtyt>inventory.min_stock
#     def display(self):
#         print(self.stock)
#         for item,qtyt in self.stock.items():
#             print(item,"below stock",inventory.check(qtyt))
#         print("total items:",self.total_items)
#         print("-"*12)
        
# a=inventory()
# b=inventory()
# a.add("apple",10)
# b.add("banana",13)
# a.display()
# b.display()

class invetory:
    total_items=0
    min_stock=5
    def __init__(self):
        self.stock={}
    def add(self,item,qty):
        self.stock[item]=qty
        invetory.total_items+=qty
    def remove(self,item,qty):
        self.stock[item]=self.stock[item]-qty
    @classmethod
    def update(cls,new):
        cls.min_stock=new
    @staticmethod
    def check(qtyt):
        return qtyt>invetory.min_stock
    def display(self):
        print(self.stock)
        for item,qtyt in self.stock.items():
            print(item,"below stock",invetory.check(qtyt))
        print("total items:",self.total_items)
        print("-"*12)
a=invetory()
b=invetory()
a.add("apple",10)
b.add("banana",13)
a.display()
b.display()

