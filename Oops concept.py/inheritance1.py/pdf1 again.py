# class animal:
#     def sound(self):
#         print("hii")
# class dog(animal):
#     def sound(self):
#         print("bow bow")
# s1=dog()
# s2=animal()
# s2.sound()
# s1.sound()


# class A:
#     def show(self):
#         print("hii")
# class B(A):
#     def show(self):
#         super().show()
#         print("how are you")
# s1=B()
# s1.show()


# class a():
#     def display(self):
#         print("hii")
# class b(a):
#     def display(self):
#         super().display()
#         print("hello")
# class c(b):
#     def display(self):
#         super().display()
#         print("how are you")
# s1=c()
# s1.display()
# print(c.mro())

# class vehicle:
#     def all(self):
#         print("all vehicles available")
# class car(vehicle):
#     def wheels(self):
#         super().all()
#         print("this is car 4 wheels")
# class bike(vehicle):
#     def wheels(self):
#         super().all()
#         print("this is bike, 2 wheels")
# s1=bike()
# s2=car()
# s1.wheels()
# print("-"*12)
# s2.wheels()


# class emp:
#     def salary(self,amount):
#         self.amount=amount
#         print("employee salary:",self.amount)
# class mang(emp):
#     def salary(self,amount,extra):
#         self.amount=amount
#         self.extra=extra
#         print("manager salary:",self.amount)
#         print("manager incentive:",self.extra)
# s1=emp()
# s2=mang()
# s1.salary(20000)
# s2.salary(30000,2000)


# class mathops:
#     @staticmethod
#     def add(a,b):
#         print(a+b)
# class adsops(mathops):
#     @staticmethod
#     def bul(x,y):
#         print(x+y)
# s1=adsops()
# s2=mathops()
# s1.bul(10,20)
# s1.add(100,20)

# class uni:
#     uni_name="jntu"
#     def shiva(self):
#         print("university name:",uni.uni_name)
#     @classmethod
#     def student(cls,new):
#         cls.uni_name=new
#         print("university name:",cls.uni_name)
# class college(uni):
#     def student(self):
#         #super().student()
#         print("hii")
# s1=college()
# s2=uni()
# s1.student()
# s2.shiva()
# s2.student("gurajada")

# def fun(n):
#     for i in range(1,n):
#         yield i
# fun(19)
# print(next())
# print(next())
# print(next())

# def fun(n):
#     for i in range(n+1):
#         yield i
# l=fun(10)
# for i in l:
#     print(i)
# # print(next(l))
# # print(next(l))
# # print(next(l))

# def fun(n):
#     for i in range(n+1):
#         yield i
# l=fun(10)
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# # for i in l:
# #     if i%2==0:
# #         print(i)

# def fun(n):
#     for i in n:
#         yield i
# l=fun("shiva")
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))

# class A:
#     def __init__(self,ph):
#         self.ph=ph
#         print('A')
# class B(A):
#     def __init__(self,roll,gen,ph):
#         self.roll=roll
#         print('B')
#         super().__init__(gen,ph)
# class C(A):
#     def __init__(self,gen,ph):
#         self.gen=gen
#         print('C')
#         super().__init__(ph)
# class D(B,C):
#     def __init__(self,name,roll,gen,ph):
#         self.name=name
#         print('D')
#         super().__init__(roll,gen,ph)
#     def display(self):
#         print(f'{self.name}\n{self.roll}\n{self.gen}\n{self.ph}')
# d1=D('Sathwik',2,'M',23456)
# # d1.display()

# n="shiva12@"
# for i in range(len(n)):
#     if n[i].isalnum():
#         print(n[i])

s="shiva"
k=s.isalpha()
print(k)