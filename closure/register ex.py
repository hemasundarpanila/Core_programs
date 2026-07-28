profile={}
def register():
    global profile
    k={}
    k["name"]=input("enter your name:")
    k["email"]=input("enter your mail:")
    k["phone no"]=input("enter your phone no:")
    while (True):
        un=input("enter your username:")
        if un in profile.keys():
            print("already exist your name")
            continue
        profile[un]=k
        print("register successfull")
        break
register()
print(profile)


profile = {}

# def register():
#     global profile

#     k = {}

#     k["name"] = input("Enter your name: ")
#     k["email"] = input("Enter your mail: ")
#     k["phone no"] = input("Enter your phone no: ")

#     while True:
#         un = input("Enter your username: ")

#         if un in profile:
#             print("Username already exists!")
#             continue

#         profile[un] = k
#         print("Registration Successful!")
#         break

# register()

# print(profile)