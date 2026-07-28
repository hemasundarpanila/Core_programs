class bank:
    def __init__(self,name,acc):
        self.name=name
        self.acc=acc
    def __hash__(self):
        return hash(self.acc)
    def __repr__(self):
        return self.name
b1=bank("sai",34567)
b2=bank("sai",34567)
k={b1,b2}
print(k)





# class student:
#     def __init__(self,marks):
#         self.marks=marks
#     def __ge__(self,o2):
#         return self.marks>=o2.marks
# s1=student(100)
# s2=student(90)
# print(s1>=s2)