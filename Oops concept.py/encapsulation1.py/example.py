# class bank:
#     def __init__(self):
#         self.bal=10000
# b=bank()
# b.bal=500000
# print(b.bal)


# class a:
#     _data=100
#     def method(self):
#         print(self._data)
# class b(a):
#     def method2(self):
#         print(self._data)
# # class c(b):
# #     def method3(self):
# #         print(self._data)
# obj=a()
# obj.method()
# print(obj._data)
# obj2=b()
# obj2.method2()
# print(obj2._data)
# # obj3=c()
# # obj3.method3()
# # print(obj3.data)


# class student:
#     def __init__(self):
#         self._name="shiva"
# class college(student):
#     def method(self):
#         print(self._name)
# class sty(college):
#     def method2(self):
#         print(self._name)
# class aa(sty):
#     def method3(self):
#         print(self._name)
# s=student()
# s2=college()
# s3=sty()
# s4=aa()
# s._name="nani"
# s2.method()
# s3.method2()
# s4.method3()
# # print(s._name)
# # print(s2._name)
# # print(s3._name)

# class Bank:
#     def __init__(self):
#         self.__balance = 10000

# b = Bank()

# # b.__balance = -50000
# print(b._balance)

# class bankaccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def check(self):
#         print(self.balance)
#     def deposit(self,n):
#         k=self.balance=self.balance+n
#         return k
# class acc(bankaccount):
#     def withdraw(self,n2):
#         if self.balance>=n2:
#             d=self.balance=self.balance-n2
#             return d
# s=bankaccount(1000)
# s2=acc(1000)
# s.check()
# print(s.deposit(500))
# print(s2.withdraw(400))

# class bank:
#     def __init__(self):
#         self.__balance=10000
#     def check(self):
#         print(self.__balance)
#     def deposite(self,amount):
#         if amount>0:
#             k=self.__balance=self.__balance+amount
#             return k
#         else:
#             print("invalid")
#     def method(self):
#         print(self.__balance+100)
# b=bank()
# b.check()
# b.method()
# # print(b._bank__balance)

# class Bank:
#     def __init__(self):
#         self.__balance = 10000

#     def check(self):
#         return self.__balance
# b = Bank()
# print(b.check())

# class Bank:
#     def __init__(self):
#         self.__balance = 10000

#     def get_balance(self):
#         return self.__balance

#     def new(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Invalid balance")
# b = Bank()
# print(b.get_balance())
# b.new(15000)
# print(b.get_balance())



# class bank:
#     def __init__(self):
#         self._balance=10000
# class savings(bank):
#     def add_interest(self):
#         self._balance=self._balance+500
#         print(self._balance)
# s=savings()
# s.add_interest()
# # print(s._balance)



# class bank:
#     def saving(self):
#         self.__balance=1000
# class extra(bank):
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             print(self.__balance)
#         else:
#             print("invalid amount")
# s=extra()
# s.withdraw(200)

# class bank:
#     def __init__(self):
#         self.__balance=1000  #self._bank__balance=1000 (internally)
#     def nani(self):
#         print(self.__balance)
# class saving(bank):
#     def shiva(self):
#         print(self.__balance)
# '''s=saving()
# s.shiva() #this is search self._saving__balance (internally)
# #so get an error'''
# s1=bank()
# s1.nani()
# print(s1._bank__balance)


# class Employee:
#     def __init__(self):
#         self.__id = 101
# class Manager(Employee):
#     def __init__(self):
#         super().__init__()
#         self.__id = 500
# s=Manager()
# print(s._Manager__id)


