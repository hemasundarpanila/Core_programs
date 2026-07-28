class inventory:
    def __init__(self,l):
        self.iv=l
    def add(self,items):
        self.iv.append(items)
    def __add__(self,o2):
        k=self.iv+o2.iv
        return inventory(k)
i1=inventory([])
i2=inventory([])
i3=inventory([])
i1.add(["apple","banana"])
i2.add(["orange"])
i3.add(["grapes"])
i4=i1+i2+i3
print(i4.iv)
