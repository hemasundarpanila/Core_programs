





# def greet():
#     x=20
#     def inner():
#         print(x)
#     return inner
# k=greet()
# k()




# def outer(): 
#     message = 'I am the outer function' 
#     def inner(): 
#         print(message)        
#     return inner  
# k=outer()               
# k()


# 

# def outer():
#     x = 100

#     def inner():
#         print(x)

#     return inner

# # k = outer()
# k()

# # def outer():
#     x = 100

#     def inner():
#         #nonlocal x
#         print(x)
#     return inner
# k=outer()
# k()
# 
# def mul(x):
#     def inner(a):
#         return a*x
#     return inner
# x=mul(3)
# y=mul(5)
# print(x(30))
# print(y(25))
# print(x.__name__)
# print(y.__name__)



# def fun(x,y):
#     z=[1,2,3]
#     def fun2(a,b):
#         print(a*y)
#         print(b,z,sep="\n")
#     return fun2
# k=fun(20,40)