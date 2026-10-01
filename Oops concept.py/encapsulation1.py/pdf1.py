# 1.  Create a BankAccount class that stores: 
# • account number 
# • balance (should not be directly modifiable) 
# You must: 
# 1. Make the balance attribute inaccessible from outside. 
# 2. Provide functions to deposit/withdraw that validate the amount. 
# 3. Prevent withdrawal if balance becomes negative. 
# 4. Show what happens if someone tries to modify balance directly and why 
# encapsulation prevents it.

# class bankaccount:
#     def __init__(self,ac_no,balance):
#         self.ac_no=ac_no
#         self.__balance=balance
#     def get(self):
#         return self.__balance
#     def deposite(self,amount):
#         print("deposited:",amount)
#         k=self.__balance=self.__balance+amount
#         return k
#     def withdraw(self,amount):
#         print("withdraw:",amount)
#         if self.__balance>=amount:
#             d=self.__balance=self.__balance-amount
#             return d
#         else:
#             print("invalid")
#     def check(self):
#         print("cheking:",self.__balance)
# s=bankaccount(1234567890,5000)
# print("main balance:",s.get())
# print("some amount deposite:",s.deposite(2000))
# print("some amount withdraw:",s.withdraw(5000))
# s.check()
# s.__balance=200000
# print("direct value:",s.__balance)
# print("main value:",s.get())

# 2. Design a Student class where marks: 
# • should always be between 0 and 100 
# • should never be set directly 
# Enable updating marks only through a controlled method that performs range 
# checks. 
# Demonstrate: 
# • trying to assign marks manually 
# • why encapsulation protects invalid states


# class student:
#     def __init__(self,marks):
#         if 0<marks<100:
#             self.__marks=marks
#         else:
#             print("Invalid..")
#     def get(self):
#         return self.__marks
#     def set(self,mark):
#         if 0<mark<100:
#             k=self.__marks=mark
#             return k
#         else:
#             print("invalid")
# s=student(55)
# print("present marks:",s.get())
# s.__marks=65
# print("manuvally assighed:",s.__marks)
# print("present marks:",s.get())
# print("update marks:",s.set(44))
# print("present marks:",s.get())


# 3. Create a SecureFile class that: 
# • stores content privately 
# • provides a method read(password) 
# • refuses access if the password is incorrect 
# • logs an "Unauthorized attempt" internally (cannot be accessed from outside)

# class securefile:
#     def __init__(self):
#         self.__password="1234"
#     def read(self,password2):
#         if self.__password==password2:
#             print("currect")
#         else:
#             print("incorrect")
# s=securefile()
# s.read(12345)

# class securefile:
#     def __init__(self,content,password):
#         self.__content=content
#         self.__password=password
#         self.__logs=[]
#     def read(self,password):
#         if self.__password==password:
#             return self.__content
#         else:
#             self.__logs.append("unauthorized attempt")
#             print("access denied")
#     def show_logs(self):
#         print(self.__logs)
# s=securefile("password is secrete","1234")
# print(s.read("1234"))
# s.read("4565")
# s.show_logs()


# class employee:
#     def __init__(self,salary):
#         self.__salary=salary
#         self.__logs=[]
#     def get(self):
#         self.__logs.append("salaryaccess attempt")
#         return self.__salary
#     def update(self,sal):
#         if sal>self.__salary:
#             k=self.__salary=sal
#             print("successfully complete")
#             return k
#         else:
#             print(" salary not decrese")
#     def check(self):
#         print(self.__logs)
# s=employee(2000)
# print("salary:",s.get())
# print("salary update:",s.update(3000))
# print("salary:",s.get())
# print("salary update:",s.update(1000))
# print("salary:",s.get())
# print("salary update:",s.update(5000))
# s.check()
    

# 5. Create a Product class where: 
# • price cannot be negative 
# • discount cannot exceed 70% 
# • internal final price calculation should not be directly exposed 
# Provide only one public method get_final_price(). 


# class product:
#     def __init__(self,price,discount):
#         if price>0 and discount<=70:
#             self.__price=price
#             self.__discount=discount
#         else:
#             print("its negative value or discount con not exceed 70")
#     # def get(self):
#     #     print("product price:",self.__price)
#     #     print("discount on product:",self.__discount)
#     def get(self):
#         k=(self.__discount/100)*self.__price
#         g=self.__price=self.__price-k
#         return g
#     def get_final_price(self):
#         print("final price:",self.__price)
# s=product(500,35)
# s.get()
# s.get_final_price()


# 6. Create a Character class with: 
# • private _health 
# • methods to damage(points) and heal(points) 
# • health cannot drop below 0 or exceed max limit 
# • expose only current health through a read-only getter




# class A:
#     def __init__(self):
#         self._x=5
#         self.__y=10
#     def getx(self):
#         if input()=="1234":
#             return self._x
#         return None
#     def setx(self, value):
#         if value >27:
#             self._x=value
#         else:
#             print("value of x should be greater than 27")
#     @property
#     def shiva(self):
#         return self._x
#     @shiva.setter
#     def fs(self, value):
#         self._x=value
#     def gety(self):
#         return self.__y
#     def sety(self, value):
#         self.__y=value
# obj=A()

# # obj.fs=10
# print(obj.getx())
# print(obj._x)
# print(obj._A__y)#name mangling
# print(obj.getx())
# print(obj.gety())
# obj.setx(100)

# print(obj.getx())



# class BankAccount:
#     def __init__(self,name):
#         self.name=name
#         self._balance=0
#         self.__atmpin="1234"
#     def getbalance(self):
#         return self._balance
#     def setpin(self,pin):
#         if input("enter previous atm pin: ")==self.__atmpin:
#             k=self.__atmpin=pin
#             return k
#         else:
#             print("pin incorrect")
# class UPI(BankAccount):
#     def sendmoney(self,amount):
#         if self._balance>amount:
#             self._balance=self._balance-amount
#         else:
#             print("insufficient balance")
#     def receivemoney(self,amount):
#         self._balance=self._balance+amount
# b1=BankAccount("madhu")
# print(b1.getbalance())
# upi=UPI("shiva")
# print(upi.getbalance())
# upi.sendmoney(100)
# upi.receivemoney(1000000000000)
# upi.sendmoney(100)
# print(upi.getbalance())

# print(b1.setpin("12345"))
# b1.setpin("3456")



# class character:
#     def __init__(self,health):
#         self.__health=health
#         self.max_limit=100
#     def damage(self,p):
#         if self.__health>=p:
#             k=self.__health=self.__health-p
#             return k
#         else:
#             print("insufficient value")
#     def heal(self,p):
#         if self.__health+p<=100:
#             q=self.__health=self.__health+p
#             return q
#         else:
#             print("Invalid")
#     def read(self):
#         return self.__health
# s=character(30)
# print("actual health:",s.read())
# print("after damage",s.damage(20))
# print("after heal",s.heal(40))
# print("present health",s.read())



# class engine:
#     def __init__(self,temp):
#         self.__temp=temp
# class car:
#     def __init__(self,value):
#         self.value=value
#     def start_car(self,value):
#         self.__temp=self.__temp+value
#     def cool_engine(self,value):
#         self.__temp=self.__temp-value
# s=



# class engine:
#     def __init__(self,type):
#         self.type=type
#         self.__temp=32
#     def cool(self):
#         print("engine cool")
#         d=self.__temp=self.__temp-10
#         print(d)
#     def start(self):
#         print("started")
#         k=self.__temp=self.__temp+10
#         print(k)
# class car:
#     def __init__(self,brand,engine):
#         self.brand=brand
#         self.engine=engine
#     def start_car(self):
#         self.engine.start()
#     def stop_car(self):
#         self.engine.cool()
# s=car("fual",engine("v12"))
# s.start_car()
# s.stop_car()



class a:
    def __init__(self):
        self.__x=5
    @property
    def fi(self):
        return self.__x
    @fi.setter
    def g(self,nx):
        if nx<10 and nx>0:
            self.__x=nx
s=a()
print(s.fi)
s.g=7
print(s.fi)

    