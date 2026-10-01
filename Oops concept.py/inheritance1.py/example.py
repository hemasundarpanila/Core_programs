# class user:
#     def __init__(self,name,dob):
#         self.name=name
#         self.dob=dob
#     def login(self):
#         print(f"{self.name} successfully login")
#     def logout(self):
#         print(f"{self.name} successfully logout")
# s1=user("shiva","2020-09-11")
# s1.login()
# s1.logout()
# class student(user):
#     def exam(self):
#         print(f"exam ettented at {self.dob}")
# s1=student("shiva","2020-09-11")
# # s1.login()
# s1.exam()
# # s1.logout()


# class user:
#     def __init__(self,name,date):
#         self.name=name
#         self.date=date
#     def login(self):
#         print(f"{self.name} successfully login")
#     def logout(self):
#         print(f"{self.name} successfully logout")
# class insta(user):
#     def post(self):
#         print(f"photo posted at  {self.date}")
# class insta2(user):
#     def show(self):
#         print(f"all {self.name} post's analysis")
# s1=insta2("shiva","2020-09-11")
# s2=insta("shiva","2020-09-11")
# s1.login()
# s2.post()
# s1.show()

# class A:
#     def m1(self):
#         print("hii")
# class B(A):
#     def m1(self):
#         print("shiva")
#         # super().m1()
# s1=B()
# s1.m1()
# s2=A()
# s2.m1()

# class email:
#     def __init__(self,mail):
#         self.mail=mail
# class phone(email):
#     def __init__(self,phonen,mail):
#         self.phonen=phonen
#         super().__init__(mail)
# class gender(email):
#     def __init__(self,gen,phonen,mail):
#         self.gen=gen
#         super().__init__(phonen,mail)
# class name(gender,phone):
#     def __init__(self,name1,gen,phonen,mail):
#         self.name1=name1
#         super().__init__(gen,phonen,mail)
#     def display(self):
#         print("student name:",self.name1, "\nstudent gender:",self.gen,"\nstudent phone no:",self.phonen,"\nstudent email:",self.mail)
# s1=name("shiva","male",8765432,"shiva@gmail.com")
# s1.display()


# def fun():
#     def fun2():
#         print("hello")
#     return fun2
# k=fun()
# k()


