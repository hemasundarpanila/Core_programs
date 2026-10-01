# class User:
#     def __init__(self,n,a,g,dob):
#         self.name = n
#         self.age = a
#         self.gender = g
#         self.Dob = dob

#     def login(self):
#         print("Login Successful")

#     def logout(self):
#         print("Logout Successful")

# class Instagram(User):
#     def post(self):
#         print(f"{self.name} post")
#         print("Got 1L likes")

# # i1 = Instagram("vidhya",21,"Female","26 Jan 2005")
# print(Instagram.mro())
# # i1.post()
# # i1.login()
# # i1.logout()
# class Restaurants:
#     def __init__(self,name,rating,address):
#         self.name = name
#         self.rating = rating
#         self.address = address

#     def display_menu(self):
#         print("All dishes are non-veg only")
# class Dish:
#     pass
# class Swiggy(User, Restaurants, Dish):
#     def display(self):
#         print("User details")
# # print(Swiggy.mro())
# class Zomato(User, Restaurants):
#     def display(self):
#         print("Zomato")

# class Customer(Swiggy, Zomato):
#     def order(self):
#         print("Just Ordering")
# print(Customer.mro())
# # s1 = Swiggy("Raj",21,"Male","1 Jan 2004")
# # s1.login()
# # s1.display_menu()
# # s1.logout()
# # s1.display()

# class Bank(User):
#     Name = "RBI"
#     def guidelines(self):
#         print("Beware of Scammer and call xxx")

# class BhimUPI(Bank):
#     def Payments(self,amount):
#         print(f"{amount} has be paid through UPI")

# b1 = BhimUPI("Nikhil",21,"Male","2 Feb 2004")
# b2 = Bank("Adi",21,"Male","3 Mar 2004")
# # print(BhimUPI.mro())



# class Instagram:
#     usernames = {}
#     def __init__(self,name,username,age,gender,psd):
#         self.name = name
#         self.username = username
#         self.age = age
#         self.gender = gender
#         self.password = psd
#         self.followers = 0
#         self.following = 0
#         self.friends_list = []
#         self.logged = False
#         Instagram.usernames[username] = self

#     @classmethod
#     def signup(cls):
#         name = input("Enter your Name: ")
#         while True:
#             username = input("Enter your username: ")
#             if username in Instagram.usernames.keys():
#                 print("Username already registered try another one")
#                 continue
#             break
#         psd = input("Enter Your Password: ")
#         age = input("Enter your age: ")
#         gender = input("Enter your gender(Male/Female): ")
#         return cls(name,username,age,gender,psd)

#     def login(self):
#         if self.logged:
#             print("Already logged in")
#         else:
#             user = input("Enter your username:")
#             password = input("Enter your password:")
#             if user == self.username and password == self.password:
#                 self.logged = True
#                 print("Logged in Successfully")
#             else:
#                 print("Invalid Credentials")

#     def logout(self):
#         if self.logged:
#             self.logged = False
#             print("Logged out successfully")
#         else:
#             print("Already logged out")

#     def follow(self,user):
#         if self.logged:
#             if user not in self.friends_list:
#                 self.following+=1
#                 user.followers+=1
#                 self.friends_list.append(user)
#             else:
#                 print("User is already following")
#         else:
#             print("Not logged in")

#     def unfollow(self,user):
#         if self.logged:
#             if user in self.friends_list:
#                 self.following-=1
#                 user.followers-=1
#                 self.friends_list.remove(user)
#             else:
#                 print("User not Found")
#         else:
#             print("Not logged in")

#     def profile(self):
#         print(f"{self.name}'s Profile")
#         print(f"Name : {self.name}")
#         print(f"Age : {self.age}")
#         print(f"Gender : {self.gender}")
#         print(f'Following : {self.following}')
#         print(f'Followers : {self.followers}')

#     def friends_profile(self):
#         if self.logged:
#             for i,j in enumerate(self.friends_list):
#                 print(f"{i} : {j.name}")

#             l = int(input("Enter your choice: "))
#             self.friends_list[l].profile()
#         else:
#             print("Not logged in")

# i1 = Instagram("Cherry","Charan",23,"Male","Hello123")
# i1 = Instagram.signup()
# i2 = Instagram("MK","Murali",23,"Male","Hello243")
# i2 = Instagram.signup()
# # i3 = Instagram.signup()
# # i4 = Instagram.signup()
# Instagram.login(i1)
# i2.login()
# i1.follow(i2)
# # i1.follow(i3)
# # i1.follow(i4)
# # i1.profile()
# # i1.friends_profile()
# # i2.unfollow(i1)
# # i3.follow(i2)
# # i3.friends_profile()



# class user:
#     def r1(self):
#         print("hii")
# class rest(user):
#     def r2(Self):
#         super().r1()
#         print("hello")
# class swiggy(rest):
#     def r3(self):
#         super().r2()
#         print("how are you")
# s1=swiggy()
# s1.r3()
# # r1=rest()
# # r1.order()

# class user:
#     def m1(self):
#         print("hii")
# class name(user):
#     def m2(self):
#         print("shiva")
#         super().m1()
# class branch(name):
#     def m3(self):
#         print("cse")
# s1=branch()
# s1.m2()