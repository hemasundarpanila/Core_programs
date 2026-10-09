'''2. Design a Student class where marks: 
• should always be between 0 and 100 
• should never be set directly 
Enable updating marks only through a controlled method that performs range 
checks. 
Demonstrate: 
• trying to assign marks manually 
• why encapsulation protects invalid states'''

# class student:
#     def __init__(self,marks):
#         if 0<marks<100:
#             self.__marks=marks
#         else:
#             print("invaalid marks")
#     def get(self):
#         return self.__marks
#     def set(self,mark):
#         if 0<mark<100:
#             k= self.__marks=mark
#             return k
#         else:
#             return "update value is invalid"
# s=student(40)
# print("present marks:",s.get())
# print("manually change marks:",s.set(150))
# print("now present marks:",s.get())
# s.__marks=65
# print("direct accesse:",s.__marks)


'''
4.Design an Employee class where: 
• salary is hidden 
• outsiders cannot read salary directly 
• use getter method that logs each access attempt 
• provide a method to update salary but only if the new salary is higher (prevent 
accidental downgrade) '''

# class employee:
#     def __init__(self,salary):
#         self.__salary=salary
#     def get_value(self):
#         return self.__salary
#     def set_value(self,value):
#         if value>self.__salary:
#             self.__salary=value
#             return self.__salary
#         else:
#             return "insufficient value"
# s=employee(10000)
# print("employee salary:",s.get_value())
# print("update salary:",s.set_value(11000))
# print("after update:",s.get_value())
        

# class student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def set_marks(self,mark):
#         if 0<mark<100:
#             self.__marks=mark
#             return self.__marks
#         else:
#             return "invalid marks"
#     def get_marks(self):
#         return self.__marks
# s=student(77)
# print("present marks:",s.get_marks())
# print("update marks:",s.set_marks(190))
# print("after update:",s.get_marks())

# class bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#         print("current balance is:",self.__balance)
#     def deposit(self,amount):
#         self.__balance+=amount
#         print("Deposited Amount is:",amount) 
#     #def get_balance(self):
#         #print("After deposit balance is:",self.__balance)
#     def withdraw(self,amount):
#         if amount<self.__balance:
#             self.__balance-=amount
#             print("Withdraw amount is:",amount) 
#         else:
#             print("Invalid amount")
#     def get_balance1(self):
#         print("Final balance is:",self.__balance)
# b=bankaccount(10000)
# b.deposit(1000)
# b.withdraw(1100)
# b.get_balance1()









