def bold(func): 
    def wrapper(*args, **kwargs): 
        return "**" + func(*args, **kwargs) + "**" 
    return wrapper 
def italic(func): 
    def wrapper(*args, **kwargs): 
        return "_" + func(*args, **kwargs) + "_" 
    return wrapper 
@bold         
@italic         
def message(): 
    return "Hello" 
print(message()) 




# import functools

# def ann(func):
#     @functools.wraps(func)
#     def inner(x,y):
#         # print(func.__name__)
#         # print(func.__annotations__)
#         # print(func.__doc__)
#         print(x,y)
#         return func(x,y)
#     return inner


# @ann
# def fun(a:int,b:int) -> int:
#     """Just adding a Doc for the function"""
#     return a+b

# print(fun(10,24))
# print(fun.__name__)
# print(fun.__annotations__)
# print(fun.__doc__)






# def fun(func):
# #     special_char=["@","#","$","%","^","&"]
#     uns=[]
#     def inner(us,pas,age):
#         nonlocal uns
        
#         if us not in uns:
#             if age>=18:
#                 k=list(filter(lambda x:x in special_char,pas))
#                 h=list(filter(lambda x:x.isdigit(),pas))
#                 g=list(filter(lambda x:x.isupper(),pas))
#                 print(k)
#                 print(h)
#                 print(g)
#                 return func(us,pas,age)
#             else:
#                 print("age is grater 17 years")
#         else:
#             print("already exist")
    
