def valid(func):
    # uns = []
    special_char = ['@',"!","#","$","%","^","&","*"]
    def inner(us,psd:str):
        if 8 <= len(psd) <= 15:
            k = list(filter(lambda x: x in special_char, psd))
            n = list(filter(lambda x: x.isdigit(), psd))
            up = list(filter(lambda x: x.isupper(), psd))
            print(k)
            print(n)
            print(up) 
            if up and n and k:
                return func(us,psd)
            else:
                return "Invalid Password"
        else:
            return "Minimum length of the password is 8 characters"
    return inner
    
@valid#register=valid(register)
def register(username,password):
     return f"{username}'s Register Successful"

print(register("shiva","Shiva@2005"))







# def fun(shiva):
#     def inner(a,b):
#         print(a+b)
#         shiva()
#         print(a-b)
#     return inner
# @fun
# def fun2():
#     print("tinnava")
# # fun2=fun(fun2)
# fun2(10,20)




# def login(func):
#     def inner():
#         un = input("Username: ")
#         psd = input("Password: ")
#         if un == "hema" and psd == "venkey":
#             print("Login Successful")
#             return func()
#         else:
#             return "Invalid Credentials"
    
#     return inner


# @login#securefile=login(securefile)
# def securefile():
#     return "Secret File"

# print(securefile())


# def fun(shiva):
#     def inner():
#         print("function is starting..")
#         shiva()
#     return inner
# @fun
# def fun2():
#     print("welcome")
# fun2()


# def fun(shiva):
#     def inner(n):
#         print("function is starting..")
#         shiva(n)
#         print("function is ending..")
#     return inner
# @fun
# def fun2(n):
#     print(f"welcome {n}")
# fun2("hemasundar")
