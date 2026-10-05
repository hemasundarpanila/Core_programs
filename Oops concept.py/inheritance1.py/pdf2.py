'''1. Bank Management System 
Create a Bank class with: 
• balance variable 
• deposit() 
• withdraw() 
• check_balance() 
Create a User class that inherits Bank and displays the user's name. Perform 
deposit, withdrawal, and balance check.

'''
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
#         print("available balance:",self.balance)
# class user(bank):
#     def __init__(self,bal,name):
#         self.name=name
#         # self.balance=bal
#         super().__init__(bal)
#     def display(self):
#         print("user name:",self.name)
#         print("present balance:",self.balance)
# s=user(5000,"shiva")
# s.display()
# s.deposite(int(input("deposite value enter:")))
# s.check_balance()
# s.withdraw(int(input("withdraw value enter:")))
# s.check_balance()    

'''2. Employee Salary System 
Create an Employee class with: 
• emp_name  
• salary 
• display_details() 
Create a Manager class that inherits Employee and adds a bonus(). Display the 
total salary.
'''

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




'''Create a Student class with: 
• Name  
• marks 
• display_marks() 
Create a Result class that inherits Student and calculates whether the student has 
passed or failed.'''

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

'''4. Food Ordering System Using Multilevel Inheritance 
Class 1: Restaurant 
• Create a method menu(item) that returns the price of the selected food 
item.  
Class 2: FoodCourt (inherits Restaurant) 
Create the following methods: 
• display_menu() – Display the available food items.  
• order() – Accept the food item from the user and allow multiple orders.  
• billing() – Display the total bill and add a packing charge of ₹20.  
Class 3: Customer (inherits FoodCourt) 
• Create an object of the Customer class.  
• Call the order() method. 
'''
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


# class movie:
#     def ticket(self,title):
#         if title=="1":
#             return 100
#         elif title=="2":
#             return 200
#         elif title=="3":
#             return 300
# class booking(movie):
#     def movies(movies):
#         print("total movies list: ")
#         print("1.khaleja "  \
#         "2.bahubali "  \
#         "3.irumudi")
#     def selection(self):
#         k=input("select movie no:")
#         g=int(input("number of tickets:"))
#         total=self.ticket(k)*g
#         print("total amount:",total)
# class customer(booking):
#     def method(self):
#         print("customer booking tickets:")
#         super().movies()
#         super().selection()
# s1=customer()
# #s1.movies()
# s1.method()



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




# class person:
#     def __init__(self,name):
#         self.name=name
# class mobile(person):
#     def __init__(self,phone,name):
#         self.phone=phone
#         super().__init__(name)
# class mail(person):
#     def __init__(self,email,phone,name):
#         self.email=email
#         super().__init__(phone,name)
# class genders(mail,mobile):
#     def __init__(self,gender,email,phone,name):
#         self.gender=gender
#         super().__init__(email,phone,name)
#     def display(self):
#         print("person name:",self.name,"\nperson mobile number:",self.phone,"\nperson email:",self.email,"\nperson gender:",self.gender)
# s=genders("male","shivapanila@gmail.com","1234567890","shiva")
# s.display()
# print(genders.mro())


'''4. Food Ordering System Using Multilevel Inheritance 
Class 1: Restaurant 
• Create a method menu(item) that returns the price of the selected food 
item.  
Class 2: FoodCourt (inherits Restaurant) 
Create the following methods: 
• display_menu() – Display the available food items.  
• order() – Accept the food item from the user and allow multiple orders.  
• billing() – Display the total bill and add a packing charge of ₹20.  
Class 3: Customer (inherits FoodCourt) 
• Create an object of the Customer class.  
• Call the order() method. '''


# class restarent:
#     def menu(self,item):
#         if item=="1":
#             return 300
#         if item=="2":
#             return 200
#         if item=="3":
#             return 100
# class foodcourt(restarent):
#     def display_menu(self):
#         print("1.biryani\n 2.pizza \n 3.ice-creame")
#     def order(self):
#         self.total=0
#         g=int(input("number of orders:"))
#         for i in range(g):
#             k=input("enter type of order:")
#             price=self.menu(k)
#             self.total+=price
#     def billing(self):
#         print("total:",self.total)
#         print("packing charge:20")
#         print("total bill:",self.total+20)
# class customer(foodcourt):
#     def __init__(self):
#         pass
# s=customer()
# s.display_menu()
# s.order()
# s.billing()

'''6. Online Course Enrollment System Using Multilevel Inheritance 
Class 1: Course 
• Create a method fee(course) that returns the course fee.  
Class 2: Academy (inherits Course) 
Create the following methods: 
• courses() – Display available courses.  
• enroll() – Allow the user to enroll in multiple courses.  
• billing() – Display the total fee and add a registration fee of ₹100.  
Class 3: Student (inherits Academy) 
• Create an object and call the enroll() method. 
'''

# class Academy(Course):
#     def courses(self):
#         print("1. Python")
#         print("2. Java")
#         print("3. SQL")
#     def enroll(self):
#         self.total = 0
#         n = int(input("Number of courses: "))
#         for i in range(n):
#             course = input("Enter course number: ")
#             price = self.fee(course)
#             self.total += price
#     def billing(self):
#         total_bill = self.total + 100
#         print("Course fee:", self.total)
#         print("Registration fee:", 100)
#         print("Total fee:", total_bill)
# class Student(Academy):
#     def __init__(self):
#         pass
# s = Student()
# s.courses()
# s.enroll()
# s.billing()

'''7. Cab Booking System Using Hierarchical Inheritance 
Class 1: Cab 
• Create methods to calculate the fare for Bike, Auto, and Car rides.  
Class 2: Uber (inherits Cab) 
• Create the methods menu(), booking(), and billing().  
• Add 10% GST and apply a 15% discount if the bill is above ₹1000.  
Class 3: Ola (inherits Cab) 
• Create the methods menu(), booking(), and billing().  
• Add 12% GST and apply a 20% discount if the bill is above ₹1500.  
Driver Code 
• Ask the user to choose Uber or Ola and call the booking() method.
'''

# class cab:
#     def bike(self,distance):
#         return distance*10
#     def auto(self,distance):
#         return distance*15
#     def car(self,distance):
#         return distance*20
# class uber(cab):
#     def menu(self):
#         print("1.bike\n 2.auto\n 3.car")
#     def booking(self):
#         choice=input("choice enter:")
#         distance=int(input("distance enter:"))
#         if choice=="1":
#             self.fare=self.bike(distance)
#         elif choice=="2":
#             self.fare=self.auto(distance)
#         elif choice=="3":
#             self.fare=self.car(distance)
#         else:
#             print("invaalid choice")
#     def billing(self):
#         gst=self.fare*10/100
#         bill=self.fare+gst
#         if bill>1000:
#             dis=bill*15/100
#             bill=bill-dis
#         print("fare:",self.fare)
#         print("gst:",gst)
#         print("final bill:",bill)
# s=uber()
# s.menu()
# s.booking()
# s.billing()


'''11. Paytm Application Using Multiple Inheritance 
Write a Python program to implement a Paytm Application using multiple 
inheritance. 
Class 1: MobileRecharge 
• Create the methods recharge_plans() and mobile_recharge().  
Class 2: BusTicketBooking 
• Create the methods display_buses() and book_ticket().  
Class 3: ElectricityBills 
• Create the methods bill_details() and pay_bill().  
Class 4: Paytm (inherits MobileRecharge, BusTicketBooking, and 
ElectricityBills) 
Create the following methods: 
• menu() – Display the available services.  
• services() – Allow the user to choose and use any service (Mobile 
Recharge, Bus Ticket Booking, or Electricity Bill Payment).
'''


# class mobilerecharge:
#     def recharge_plan(self,plan):
#         if plan=="1":
#             return 150
#         elif plan=="2":
#             return 300
#         elif plan=="3":
#             return 500
#     def mobile_recharge(self):
#         print("1.only voice call\n 2.only data 2gb\n 3.voice call and data 5g")
#         n=input("enter plan type:")
#         k=int(input("total months:"))
#         total=self.recharge_plan(n)*k
#         print("total amount:",total)
# class bus_ticket:
#     def display_bus(self,bus):
#         if bus=="1":
#             return 500
#         elif bus=="2":
#             return 1000
#         elif bus=="3":
#             return 1200
#     def book_ticket(self):
#         print("1.Non ac bus\n 2.Ac bus\n 3.Ac with food free")
#         p=input("enter bus type:")
#         q=int(input("enter total tickets:"))
#         total=self.display_bus(p)*q
#         print("total amount:",total)
# class paytm(mobilerecharge,bus_ticket):
#     def menu(self):
#         print("1.Mobile recharge\n 2.Bus ticket")
#     def service(self):
#         m=input("enter service type:")
#         if m=="1":
#             super().mobile_recharge()
#         elif m=="2":
#             super().book_ticket()
#         else:
#             print("invaalid type")
# s=paytm()
# s.menu()
# s.service()
