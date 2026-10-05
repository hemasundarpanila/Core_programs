'''Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that 
override it. 
Demonstrate polymorphism by iterating over a list of different animal objects and calling 
make_sound().
'''
# class animal:
#     def make_sound(self):
#         print("hiii")
# class dog(animal):
#     def make_sound(self):
#         print("dark")
# class cat(animal):
#     def make_sound(self):
#         print("meaw")
# class cow(animal):
#     def make_sound(self):
#         print("amma")
# l=[dog(),cat(),cow()]
# for i in l:
#     i.make_sound()
 
'''Write a function operate(device) that calls device.start(). 
Pass in objects of Car, Computer, and WashingMachine — all of which define a start() 
method, but share no inheritance relationship. 
Show that Python’s polymorphism works through behavior, not type. '''

# class car:
#     def start(self):
#         print("car")
# class computer:
#     def start(self):
#         print("computer")
# class washing:
#     def start(self):
#         print("washing")
# def operate(device):
#     device.start()
# s1=operate(car())
# s1=operate(computer())
# s1=operate(washing())


'''Create a Vector class that supports: 
• + operator → add coordinates 
• == operator → compare equality 
Show how operator overloading gives natural polymorphism to user-defined classes.'''
    

# class vector:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def __str__(self):
#         return f"{self.num1,self.num2}"
#     def __add__(self,other):
#         return vector(self.num1+other.num1,self.num2+other.num2)
#     def __eq__(self,other):
#         return self.num1==other.num1 and self.num2==other.num2
# s1=vector(40,20)
# s2=vector(90,50)
# s3=vector(60,50)
# print(s1+s2+s3)
# print(s1==s2)

# class name:
#     def student(self):
#         print("hii")
# class name2:
#     def student(self):
#         print("shiva")
# def check(value):
#     value.student()
# # value=[name(),name2()]
# # for i in value:
# #     i.student()
# s1=name()
# s2=name2()
# check(s1)
# check(s2)

# class user:
#     def __init__(self,marks):
#         self.marks=marks
#     def __str__(self):
#         return str(self.marks)
#     def __add__(self,other):
#         return user(self.marks+other.marks)
# s1=user(20)
# s2=user(30)
# s3=user(30)
# print(s1+s2+s3)


# class animal:
#     def make_sound(self):
#         print("hii")
# class dog(animal):
#     def make_sound(self):
#         print("bow bow")
# class cat(animal):
#     def make_sound(Self):
#         print("meaw")
# class cow(animal):
#     def make_sound(self):
#         print("amma")
# value=[dog(),cat(),cow()]
# for i in value:
#     i.make_sound()

# class car:
#     def start(self):
#         print("car")
# class computer:
#     def start(self):
#         print("computer")
# class washing:
#     def start(self):
#         print("washing amchine")
# def operate(device):
#     device.start()
# s1=car()
# s2=computer()
# s3=washing()
# operate(s1)
# operate(s2)
# operate(s3)

# class vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return f"{self.x},{self.y}"
#     def __add__(self,other):
#         return vector(self.x+other.x,self.y+other.y)
# s1=vector(10,20)
# s2=vector(30,40)
# s3=vector(30,40)
# print(s1+s2+s3)

# class transport:
#     def move(self):
#         print("hii")
# class bus(transport):
#     def move(self):
#         print("bus")
#         super().move()
# class bike(transport):
#     def move(self):
#         print("bike")
#         super().move()
# s1=bike()
# s2=bus()
# s1.move()
# print()
# s2.move()

# class bs:
#     def logic(self,data):
#         print("bouble sort")
#         return sorted(data)
# class ms:
#     def logic(self,data):
#         print("merge")
#         return sorted(data)
# class sort:
#     def change(self,state,data):
#         return state.logic(data)
# num=[5,2,4,7,8]
# s=sort()
# print(s.change(bs(),num))
# print(s.change(ms(),num))

# class vector:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def __str__(self):
#         return f"{self.num1,self.num2}"
#     def __add__(self,ot):
#         return vector(self.num1+ot.num1,self.num2+ot.num2)
# s1=vector(0,2)
# s2=vector(3,4)
# s3=vector(5,10)
# s4=vector(20,30)
# print(s1+s2+s3+s4)
        

class account:
    def withdraw(self,amount):
        self.amount=amount
        print("withdraw amount:",self.amount)
class savingaccount(account):
    def withdraw(self):
        print("withdraw")
class premiumsaving(savingaccount):
    def withdraw(self):
        return super().withdraw()

