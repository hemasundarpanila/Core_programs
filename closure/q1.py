#employe salary bonus
def fun(salary):
    def inner(percentage):
        total=salary+salary*percentage/100
        return total
    return inner
a=fun(30000)
print(a(10))




#shopping example
# def fun():
#     total=0
#     def inner(price):
#         nonlocal total
#         total=total+price
#         return total
#     return inner
# a=fun()
# print(a(100))
# print(a(200))
# print(a(300))



#Calculator using closures.
# def fun(x):
#     def inner(op,y):
#         if op=="+":
#             return x+y
#         elif op=="-":
#             return x-y
#         elif op=="*":
#             return x*y
#         elif op=="/":
#             return x/y
#         else:
#             return x//y
#     return inner
# a=fun(10)
# print(a("+",20))
# print(a("-",20))
# print(a("*",20))
# print(a("/",20))
# print(a("//",20))
      


#Store marks using a closure.
# def fun(m):
#     def inner():
#         print("marks:",m)
#     return inner
# a=fun(56)
# a()



#Create a counter using nonlocal.
# def fun():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner
# a=fun()
# print(a())
# print(a())


#Create a greeting closure.
# def fun(name):
#     def inner():
#         print(f" Happy Birthday {name}")
#     return inner
# a=fun("Sai Ganesh")
# a()


#Create a multiplier closure.
# def fun(x):
#     def inner(y):
#         return x*y
#     return inner
# a=fun(5)
# b=fun(7)
# print(a(6))
# print(b(2))




#Create a closure that adds 10 to a number.
# def fun(y):
#     def inner(x):
#         s=x+y
#         print(s)
#     return inner
# a=fun(10)
# a(20)






#Create a closure that prints a name.
# def fun(x):
#     def inner():
#         print(x)
#     return inner
# a=fun("shiva")
# a()