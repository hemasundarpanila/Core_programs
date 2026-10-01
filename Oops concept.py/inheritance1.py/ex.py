# class user:
#     def login(self):
#         print("successfully login")
#     def logout(self):
#         print("uccessfully logout")
# class instagram(user):
#     def post(self):
#         print("photo posted")
# class facebook(user):
#     def like(self):
#         print("one like")
# a=instagram()
# b=facebook()
# a.login()
# a.post()
# b.login()
# b.like()

# class user():
#     def __init__(self,name,age,gender,dob):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.dob=dob
#     def login(self):
#         print("successfully login")
#     def logout(self):
#         print("successfylly log-out")
# class instagram(user):
#     def post(self):
#         print(self.name,"one post posted")
#         print("got one lack likes")
# a=instagram("shiva",21,"male","11 sep 2004")
# a.login()
# a.post()
# a.logout()



# class A:
#     def m1(self):
#         print("hii")
#     def m2(self):
#         print("hello")
# class B(A):
#     def m3(self):
#         print("happy")
# a=B()
# b=A()
# a.m1()
# a.m2()
# a.m3()
# print("-"*12)
# b.m1()
# b.m2()
# b.m3()


# class A:
#     def m1(self):
#         print("m1 class")
# class B(A):
#     def m1(self):
#         print("hello")
# a=A()
# b=B()
# a.m1()
# b.m1()


# class land_animal:
#     def being(self):
#         print("land animals")
# class water_animal:
#     def water(self):
#         print("water animals")
# class frog(land_animal,water_animal):
#     def living(self):
#         self.being()
#         self.water()
#         print("both water and land")
# a=frog()
# # a.being()
# # a.water()
# a.living()
