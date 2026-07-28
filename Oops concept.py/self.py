class student:
    def __init__(self,name,age,background):
        self.name=name
        self.age=age
        self.background=background
    def about(self):
        print("my name is",self.name)
        print("my age is",self.age)
        print("my background is",self.background)
        print("_"*15)
a=student("shiva",21,"cse")
b=student("nani",23,"csm")
a.about()
b.about()










# class student:
#     name="shiva"
#     age=21
#     background="cse"
#     def about(self):
#         print("my name is",self.name)
#         print("my age is",self.age)
#         print("my background is",self.background)
# a=student()
# a.about()
# b=student()
# b.name="sai"
# b.age=22
# b.background="eee"
# print(a.name,a.age,a.background)
# print(b.name,b.age,b.background)