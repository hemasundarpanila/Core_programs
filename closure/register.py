profile = {}
def register():
    global profile
    k = {}
    k["name"] = input("Enter your name: ")
    k["email"] = input("Enter your email: ")
    k["phno"] = input("Enter your phone number: ")
    while True:
        un = input("Enter username: ")

        if un in profile:
            print("Username already exists!")
            continue
        profile[un] = k
        print("Registration Successful!")
        break
def login():
    un = input("Enter username to view details: ")
    if un in profile:
        print("User Found")
        print(profile[un])      # Only that user's details
    else:
        print("Username not found")
# Register two users
register()
register()
print("\nComplete Profile Dictionary:")
print(profile)
print("\nLogin")
login()







# profile = {"shiva":{"name":"shiva"}}
# def register():
#     global profile
#     k = {}
#     k["name"] = input("Enter your name: ")
#     k["email"] = input("Enter your email: ")
#     k["phno"] = input("Enter your phone number: ")

#     while True:
#         un = input("Enter your username: ")

#         if un in profile.keys():
#             print("Username already exists!")
#             continue

#         profile[un] = k
#         print("Registration Successful!")
#         break
# # Calling the function
# register()
# # Display all registered users
# print(profile)
