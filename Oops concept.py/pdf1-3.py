
# class Mathops:
#     def __init__(self,number):
#         self.number=number
#     @staticmethod
#     def is_num(num):
#         if num%2==0:
#             print("even")
#         else:
#             print("odd")
#     def display(self):
#         print("given number:",self.number)
#         Mathops.is_num(self.number)
# a=Mathops(20)
# b=Mathops(15)
# a.display()
# b.display()
# Mathops.is_num(20)

class MathOPs:
    def __init__(self,num):
        self.num=num
    @staticmethod
    def check(number):
        if number%2==0:
            return "even"
        else:
            return "odd"
    def display(self):
        print("number:",self.num)
        print(MathOPs.check(self.num))
a=MathOPs(20)
b=MathOPs(23)
a.display()
b.display()

