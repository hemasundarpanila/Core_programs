# def Upper(x):
#     for i in x:
#         if i.isupper():
#             return True
#     return False

def vaild(func):
    uns = []
    special_char = ['@',"!","#","$","%","^","&","*"]
    def inner(us:str,psd:str,age:int):
        nonlocal uns
        if us not in uns:
            if 8 <= len(psd) <= 15:
                k = list(filter(lambda x: x in special_char, psd))
                n = list(filter(lambda x: x.isdigit(), psd))
                up = list(filter(lambda x:x.isupper,psd))
                print(k)
                print(n)
                print(up)

                if up and n and k:
                    if age >= 18:
                        uns.append(us)
                        return func(us,psd,age)
                    else:
                        return "Age must be greater than 17"
                else:
                    return "Invalid Password"
            else:
                return "Minimum length of the password is 8 characters"
        else:
            return "Username already exists"
    return inner


@vaild
def register(username,password,age):
    return f"{username}'s Register Successful"

print(register("praveen","Dhaya143$$",19))
print(register("praveen","Dhaya143$$",19))







# def fun(fun2):
#     special_char=["@","#","$","%","^","&","*","!"]
#     def inner(us,pas:str):
#         if 8<= len(pas) <=15:
#             k=list(filter(lambda x:x in special_char ,pas))
#             h=list(filter(lambda x:x.isdigit,pas))
#             g=list(filter(lambda x:x.isupper,pas))
#             if k and h and g:
#                 return fun2(us,pas)
#             else:
#                 print("invalid")
#         else:
#             print("we need 8 characters")
#     return inner
# @fun
# def register(us,pas):
#     return f"{us}is registered successfull"
# print(register("shiva","Shiva@2005"))
