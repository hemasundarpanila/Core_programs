#no argument,no return

# def fun():
#     print("hii")
# fun()

#no argument,return
# def fun():
#     return 100
# print(fun())

#argument,no return 
# def fun(a,b):
#     print(a+b)
# fun(10,20)

#argumet,return 
# def fun(a,b):
#     return a+b
# x=fun(678,67)
# print(x)


# def fun(x,y):
#     def fun2(a):
#         print(x+y)
#     fun2(100)
# fun(10,20)   

#closure:
def fun():
    def inner():
        print("hii")
    return inner
a=fun()
a()