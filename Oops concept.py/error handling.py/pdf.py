'''Write a function named find_length(obj) that uses a loop to calculate the 
length of the given object without using the built-in len() function. The 
function should return the calculated length if the object is iterable. If a 
non-iterable object such as an integer is passed, the function should raise and 
handle a TypeError, and print an appropriate error message explaining what 
happens when an integer is sent as input.
'''

# def find_length(obj):
#     try:
#         c=0
#         for i in obj:
#             c=c+1
#         return c
#     except TypeError:
#         print("given value not iterable")
# print(find_length("hello"))
# print(find_length(100))

# class person:
#     def __init__(self,age):
#         self.age=age
#         try:
#             if age<0:
#                 raise ValueError("age must positive")
#             return age
#         except ValueError as e:
#             print(e)
# s=person(3)
# print(s.age)

# class person:
#     def __init__(self, age):
#         self.age=age
#         try:
#             if age < 0:
#                 raise ValueError("Age must be greater than or equal to 0")
#             return self.age
#         except ValueError as e:
#             print(e)
# s = person(-2)
# print(s.age)



# class person:
#     def __init__(self, age):
#         self.age = age
#         try:
#             if age < 0:
#                 raise ValueError("age must be positive")
#             return self.age
#         except ValueError as e:
#             print(e)
# s = person(-22)
# print(s)

# class person:
#     def __init__(self, age):
#         try:
#             if age < 0:
#                 raise ValueError("age must be positive")

#             self.age = age

#         except ValueError as e:
#             print(e)


# s = person(-22)

# if hasattr(s, "age"):
#     print(s.age)

# class student:
#     marks=0
#     def __init__(self,marks):
#         pass
#     def set_marks(self,marks):
#         try:
#             if self.marks<0 or 100<self.marks:
#                 raise ValueError("value must 0 to 100 between")
#             self.marks=marks
#         except ValueError as e:
#             print(e)
# s=student(200)
# print(s.marks)

'''• Create a class Person whose constructor takes age as an argument. Raise a 
ValueError if the age is less than 0.
'''

# class person:
#     def __init__(self,age):
#         if age<0:
#             raise ValueError
#         self.age=age
# P=person(-20)

'''• Write a function named find_length(obj) that uses a loop to calculate the 
length of the given object without using the built-in len() function. The 
function should return the calculated length if the object is iterable. If a 
non-iterable object such as an integer is passed, the function should raise and 
handle a TypeError, and print an appropriate error message explaining what 
happens when an integer is sent as input.
'''

# def find_length(obj):
#     c=0
#     try:
#         for i in obj:
#             c=c+1
#         return c
#     except TypeError:
#         print("Type Error:value not iterable")
# print(find_length("shiva"))
# print(find_length([1,2,3,4,5]))
# find_length(12)


'''• Create a class Student with an attribute marks. Implement a method 
set_marks(marks) that raises a ValueError if marks are not in the range 0 to 
100.
    '''

# class student:
#     def __init__(self):
#         pass
#     def set_marks(self,marks):
#         try:
#             if marks<0 or marks>100:
#                 raise ValueError("value invalid")
#             print(marks)
#         except ValueError as e:
#             print(e)
#         else:
#             print("vaalid")
# s=student()
# s.set_marks(20)

'''• Create a custom exception named InvalidAgeError. Create a class Voter with a 
method check_eligibility(age) that raises this exception if age is less than 18.
'''
# class Invalidageerror(Exception):
#     pass
# class voter:
#     def check(self,age):
#         try:
#             if age<0 or age<18:
#                 raise Invalidageerror("not a valid value")
#             print("valid:",age)
#         except Invalidageerror as e:
#             print(e)
#         else:
#             print("complete")
# s=voter()
# s.check(19) 



# class InvalidMarksError(Exception):
#     pass

# marks = 20

# try:
#     if marks < 0 or marks > 100:
#         raise InvalidMarksError("Marks must be between 0 and 100")
#     print("Valid marks:",marks)

# except InvalidMarksError as e:
#     print(e)



'''• Create a class BankAccount with an attribute balance. Implement a method 
withdraw(amount) that raises an exception if the withdrawal amount is greater 
than the available balance'''

# class Invalidbalance(Exception):
#     pass
# class bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         try:
#             if amount>self.balance:
#                 raise Invalidbalance("Bank balance must grater than withdraw amount")
#             self.balance-amount
#             print("withdra amount",amount)
#             print("after withdraw:",self.balance)
#         except Invalidbalance as e:
#             print(e)
# s=bank(1000)
# s.withdraw(1500)
    

'''• Create a class PasswordValidator with a method validate(password). Raise an 
exception if the password length is less than 8 characters'''

# class UserInput:
#     def get_integer(self, value):
#         try:
#             num = int(value)
#             print("Integer:", num)
#         except ValueError:
#             print("ValueError: Please enter a valid integer.")
#         except TypeError:
#             print("TypeError: The value cannot be converted to an integer.")
# u = UserInput()
# u.get_integer(123.3)
# u.get_integer("hello")
# u.get_integer(None)

'''• Create a base class Shape with a method area() that raises 
NotImplementedError. Create a child class Rectangle that overrides and 
implements the area method'''

# class shape:
#     def area(self):
#         raise NotImplementedError
# class rectangle(shape):
#     def __init__(self,hight,width):
#         self.hight=hight
#         self.width=width
#     def area(self):
#         return self.hight*self.width
# s=rectangle(12,24)
# print("circle rectangle:",s.area())


'''• Create a class Service with a method that calls another method which raises an 
exception. Catch and handle the exception in the Service class'''
# class serviceerror(Exception):
#     pass
# class service:
#     def shiva(self):
#         raise serviceerror("something wrong")
#     try:
#         def nani(self):
#             self.shiva()
#     except NotImplementedError as e:
#         print(e)
# s=service()
# s.nani()

'''• Create a class Transaction with a method process() that uses try, except, and 
finally blocks to ensure a cleanup message is always printed

    
    '''

# class Transaction:
#     def process(self):
#         try:
#             print("Processing transaction")
#             raise ValueError("Transaction failed")
#         except ValueError as e:
#             print("Error:", e)
#         finally:
#             print("Cleanup completed")
# t = Transaction()
# t.process()

'''• Create a class LoginSystem with a method login(password) that raises an 
exception for an incorrect password and handles the exception outside the class'''

# class LoginSystem:
#     def login(self, password):
#         if password != "python123":
#             raise ValueError("Incorrect password")
#         print("Login successful")
# user = LoginSystem()
# try:
#     user.login("hello123")
# except ValueError as e:
#     print("Login error:", e)