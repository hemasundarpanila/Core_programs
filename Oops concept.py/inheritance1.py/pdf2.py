# class bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposite(self,amount):
#         self.balance+=amount
#         print("deposite:",amount)
#     def withdraw(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             print("withdraw:",amount)
#         else:
#             print("not valiable amount")
#     def check_balance(self):
#         print(self.balance)
# class user(bank):
#     def __init__(self,bal,name):
#         self.name=name
#         self.balance=bal
#     def display(self):
#         print(self.name)
# s=user(5000,"shiva")
# s.display()
# s.deposite(2000)
# s.withdraw(500)
# s.check_balance()    

# class Emp:
#     # def __init__(self,name,exp):
#     #     self.name=name
#     #     self.exp=exp
#     def dis(self):
#         print("Emp")
#         print(self.name,self.exp,self.tester)
# class Man(Emp):
#     def __init__(self,name,exp,desig):
#         self.name=name
#         self.exp=exp
#         self.tester=desig
#     def dis(self):
#             super().dis()
#             print(self.tester)
# m = Man("shiva",2,"tester")
# m.dis()

# # Create an Employee class with: 
# # • emp_name  
# # • salary 
# # • display_details() 
# # Create a Manager class that inherits Employee and adds a bonus(). Display the 
# # total salary. 


# class employee:
#     def __init__(self,name,sal):
#         self.name=name
#         self.sal=sal
#     def display(self):
#         print("employee name:",self.name)
#         print("employee salary:",self.sal)
# class manager(employee):
#     def __init__(self,name,sal,bonus):
#         super().__init__(name,sal)
#         self.bonus=bonus
#         # self.name=name
#         # self.sal=sal
#     def new(self):
#         self.sal+=self.bonus
#         print("bonus:",self.bonus)
#         print("total balance with bonus:",self.sal)
# s=manager("shiva",30000,2000)
# s.display()
# s.new()
#print(manager.mro())

# # Create a Student class with: 
# # • Name  
# # • marks 
# # • display_marks() 
# # Create a Result class that inherits Student and calculates whether the student has 
# # passed or failed.

# # class student:
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
# #     def display(self):
# #         print("student name:",self.name)
# #         print("student marks:",self.marks)
# # class result(student):
# #     def valid(self):
# #         if self.marks>30:
# #             print("pass")
# #         else:
# #             print("fail")
# # s=result("shiva",25)
# # s.display()
# # s.valid()

# # 4. Food Ordering System Using Multilevel Inheritance 
# # Class 1: Restaurant 
# # • Create a method menu(item) that returns the price of the selected food 
# # item.  
# # Class 2: FoodCourt (inherits Restaurant) 
# # Create the following methods: 
# # • display_menu() – Display the available food items.  
# # • order() – Accept the food item from the user and allow multiple orders.  
# # • billing() – Display the total bill and add a packing charge of ₹20.  
# # Class 3: Customer (inherits FoodCourt) 
# # • Create an object of the Customer class.  
# # • Call the order() method. 

# class rest:
#     def menu(item):
#         pass
# class food(rest):
#     def display_menu(foods):
#         print("food items:",foods)
#     def order()
        
# class customer(food):
#     pass

# n=8
# c=0
# for i in range(1,n+1):
#     c=c+1
#     for j in range(1,n+1):
#         if i==1 or i==n or i==(n//2)+1:
#             print("*",end=" ")
#         elif j==1 and c<=(n//2)+1:
#             print("*",end=' ')
#         elif j==n and c>=(n//2)+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# l=[1,2,3,4,5]
# t1=l.__iter__()
# print(next(t1))

# class bank:
#     def __init__(self,balance):
#         self.balence=balance
#         print("present balance:",self.balance)
#     def deposite(self,new):
#         self.balance+=new
#         print("deposite balance:",new)
#     def withdraw(self,new2):
#         self.balance-=new2
#         print("withdraw balance:",new2)
#     def check(self):
#         print("available balance:",self.balance)
# class user(bank):
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#         print("user name:",self.name)
#         super().__init__(self.balance)
# s1=user("shiva",10000)
# s1.deposite(5000)
# s1.withdraw(2000)
# s1.check()

# class emp:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print("employee name:",self.name)
#         print("employee salary:",self.salary)
# class manager(emp):
#     def __init__(self,bonus,name,salary):
#         self.bonus=bonus
#         self.name=name
#         self.salary=salary
#         print("manager salary:",self.bonus+self.salary)
#         super().__init__(name,salary)
# s1=manager(2000,"shiva",30000)
# s1.display()


class movie:
    def ticket(self,title):
        if title=="1":
            return 100
        elif title=="2":
            return 200
        elif title=="3":
            return 300
class booking(movie):
    def movies(movies):
        print("total movies list: ")
        print("1.khaleja "  \
        "2.bahubali "  \
        "3.irumudi")
    def selection(self):
        k=input("select movie no:")
        g=int(input("number of tickets:"))
        total=self.ticket(k)*g
        print("total amount:",total)
class customer(booking):
    def method(self):
        print("customer booking tickets:")
        super().movies()
        super().selection()
s1=customer()
#s1.movies()
s1.method()



# n=input()
# l=input()
# if l not in n:
#     print(l)


#n="shiva@gmail.com"
#@k=n.find("@",1,len(n))
'''x = input('enter the string:')
res = x[::-1]
if res==x:
    print('palindrome')
else:

   print('not palindrome')'''
# n = int(input('enter the number:'))
# for d in range(2,n//2+1):
#     if n%d ==0:
#         print('not prime')
#         break
# else:
#     print('prime')
