# Question 1: Bank Account Operations
# Create a class BankAccount with:
# •	attributes: account_holder, balance 
# •	instance method: deposit(amount) 
# •	instance method: withdraw(amount) 
# Implement these magic methods:
# •	__str__() → display account details 
# •	__add__() → add balances of two accounts 
# •	__sub__() → subtract balances 
# •	__eq__() → compare if two accounts have same balance 
# •	__lt__() → check which account has lower balance 
# •	__getattribute__() → print a message whenever an attribute is accessed 
# •	__setattr__() → prevent setting negative balance 
# Demonstrate creating two accounts and using all operations




# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#     # Deposit Money
#     def deposit(self, amount):
#         self.balance += amount
#     # Withdraw Money
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Balance")
#     # Display Account Details
#     def __str__(self):
#         return f"Account Holder: {self.account_holder}\nBalance: {self.balance}"
#     # Add Balances
#     def __add__(self, other):
#         return self.balance + other.balance
#     # Subtract Balances
#     def __sub__(self, other):
#         return self.balance - other.balance

#     # Compare Equal Balances
#     def __eq__(self, other):
#         return self.balance == other.balance

#     # Compare Lower Balance
#     def __lt__(self, other):
#         return self.balance < other.balance
# # Create Objects
# a = BankAccount("Shiva", 10000)
# b = BankAccount("Nani", 8000)
# # Display Details
# print(a)
# print()
# print(b)
# # Deposit
# a.deposit(2000)
# # Withdraw
# b.withdraw(1000)
# print("\nAfter Transactions")
# print(a)
# print()
# print(b)
# # Magic Methods
# print("\nAdd Balances:", a + b)
# print("Subtract Balances:", a - b)
# print("Equal Balances:", a == b)
# print("a < b:", a < b)


class bank_account:
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
            self.balance-=amount
    def __str__(self):
         return f"holder:{self.holder}\nbalance:{self.balance}"
    def __add__(self,other):
         return bank_account("total:",self.balance+other.balance)
    def __sub__(self,other):
         return bank_account("sub:",self.balance-other.balance)
    def __eq__(self,other):
         return bank_account("equality:",self.balance==other.balance)
         
a=bank_account("shiva",10000)
b=bank_account("nani",15000)
c=bank_account("nani",20000)
# print(a)
# print(b)
# print(c)
# a.deposite(2000)
# b.deposite(3000)
# c.deposite(3000)
# print("after deposite some amount in each account:")
# print(a)
# print(b)
# print(c)
# print("withdraw some amount in each account:")
# a.withdraw(6000)
# b.withdraw(6000)
# c.withdraw(6000)
# print(a)
# print(b)
# print(c)
# print("after complete the transactions details:")
print("total amount:",a+b+c)
# print("sub amount:",a-b-c)
# print("eq:",a==b and b==c)



# Create a class Product with:
# •	attributes: name, price, quantity 
# •	method: total_price() 
# Implement:
# •	__str__() 
# •	__add__() → add total prices of two products 
# •	__mul__() → multiply product price by a number 
# •	__gt__() → compare which product has greater total value 
# •	__eq__() → compare prices 
# •	__getattr__() → return "Attribute not found" for missing attributes 
# •	__setattr__() → do not allow price less than 0 
# ________________________________________


# class product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def total(self):
#         return self.price*self.quantity
#     def __str__(self):
#         return f"name:{self.name}\nquantity:{self.quantity}\nprice:{self.total()}"
#     def __add__(self,other):
#         return self.total() + other.total()
#     def __mul__(self,number):
#         return (self.price*number)
#     def __gt__(self,other):
#         return self.total()>other.total()
#     def __eq__(self,other):
#         return self.price==other.price
# a=product("shiva",200,2)
# b=product("nani",200,3)
# print(a)
# print(b)
# print(a.total())
# print(b.total())
# print("total price:",a+b)
# print("multiple one number:",a*5)
# print("total price a>b is :",a>b)
# print("price a==b is :",a==b)


         
# Question 3: Student Marks
# Create a class Student with:
# •	attributes: name, marks 
# •	method: grade() 
# Implement:
# •	__str__() 
# •	__add__() → add marks of two students 
# •	__truediv__() → divide marks by a number 
# •	__ge__() → check if one student scored greater than or equal to another 
# •	__lt__() → check if one student scored less 
# •	__getattribute__() → track attribute access 
# •	__setattr__() → marks must be between 0 and 100 
# ________________________________________

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def grade(self):
#         if self.marks>=90:
#             print("grade:A")
#         elif self.marks>=70:
#             print("grade:B")
#         elif self.marks>=50:
#             print("grade:C")
#         elif self.marks>=30:
#             print("grade:D")
#         else:
#             print("fail")
#     def __str__(self):
#         return f"student name:{self.name}\nstudent marks:{self.marks}"
#     def __add__(self,other):
#         return self.marks+other.marks
#     def __truediv__(self,number):
#         return self.marks/number
#     def __ge__(self,other):
#         return self.marks>=other.marks
#     def __lt__(self,other):
#         return self.marks<other.marks
# a=student("shiva",56)
# b=student("raju",78)
# print(a)
# a.grade()
# print(b)
# b.grade()
# print("total marks:",a+b)
# print("division one number:",a/5)
# print("marks grater or eql check:",a>=b)
# print("lessthan check:",a<b)



# Question 4: Rectangle Area Comparison
# Create a class Rectangle with:
# •	attributes: length, breadth 
# •	method: area() 
# Implement:
# •	__str__() 
# •	__add__() → add areas of two rectangles 
# •	__sub__() → subtract areas 
# •	__eq__() → compare areas 
# •	__gt__() → check which rectangle has larger area 
# •	__getattr__() → handle missing attributes 
# •	__setattr__() → length and breadth must be positive 
# ________________________________________

# class rectangle:
#     def __init__(self,len,bre):
#         self.len=len
#         self.bre=bre
#     def area(self):
#         total=self.len*self.bre
#         return total
#     def __str__(self):
#         return f"length:{self.len}\nbreadth:{self.bre}"
#     def __add__(self,other):
#         return self.area()+other.area()
#     def __sub__(self,other):
#         sub_total=self.area()-other.area()
#         return sub_total
#     def __eq__(self,other):
#         return self.area()==other.area()
#     def __gt__(self,other):
#         return self.area()>other.area()
# a=rectangle(17,18)
# b=rectangle(15,14)
# print(a)
# print("area:",a.area())
# print(b)
# print("area:",b.area())
# print("comparition values:")
# print("add area:",a+b)
# print("equality area check:",a==b)
# print("greater area check:",a>b)

# Question 5: Employee Salary System
# Create a class Employee with:
# •	attributes: name, salary 
# •	method: annual_salary() 
# Implement:
# •	__str__() 
# •	__add__() → add salaries of two employees 
# •	__mul__() → calculate salary after multiplying by months 
# •	__ne__() → check if salaries are not equal 
# •	__le__() → check if one salary is less than or equal to another 
# •	__getattribute__() → log every attribute access 
# •	__setattr__() → salary cannot be below 10000 
# ________________________________________

# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def annual_salary(self):
#         total_salary=self.salary*12
#         return total_salary
#     def __str__(self):
#         return f"employee name:{self.name}\nemployee salary:{self.salary}"
#     def __add__(self,other):
#         return self.salary+other.salary
#     def __mul__(self,months):
#         return self.salary*months
# a=employee("shiva",30000)
# b=employee("adi",40000)
# print(a)
# print("annual salary:",a.annual_salary())
# print(b)
# print("annual salary:",b.annual_salary())
# print("add salaryes:",a+b)
# print("salary by months:7",a*7)
# print("salary by months:8",b*8)




# Question 6: Book Object Comparison
# Create a class Book with:
# •	attributes: title, author, pages 
# •	method: reading_time()
# Assume 1 page takes 2 minutes. 
# Implement:
# •	__str__() 
# •	__add__() → add pages of two books 
# •	__floordiv__() → divide pages by number of days 
# •	__gt__() → compare books based on pages 
# •	__eq__() → compare books based on title 
# •	__getattr__() → return custom message for missing attribute 
# •	__setattr__() → title cannot be empty and pages must be positive 
# ________________________________________

