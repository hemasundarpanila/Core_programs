# class user:
#     def __init__(self,n,a,g,dob):
#         self.name=n
#         self.age=a
#         self.gender=g
#         self.dob=dob
#     def login(self):
#         print('Successfully Logged in')
#     def logout(self):
#         print('successfully logged out')
# class Instagram(user):
#     def post(self):
#         print(f'{self.name} post')
#         print('got 1l likes')
# a1=Instagram('parul',15,'Male','23-07-2004')
# class rest:
#     def __init__(self,name,rating,address):
#         self.name=name
#         self.rating=rating
#         self.address=address
#     def display_menu(self):
#         print("all items are non-veg")
# class swiggy(user,rest):
#     def display(self):
#         print("user details")
# s1=swiggy("shiva",20,"male","1 jan 2005")
# s1.login()
# s1.display()
# s1.display_menu()
# s1.logout()
# class bank(user):
#     def guidelines(Self):
#         print("beware of scammer and call xxxx")
# class bhimUPI(bank):
#     def payments(self,amount):
#         print(f"{amount} has be paid through upi")
# b1=bhimUPI("nani",21,"male","5 jan 2003")
# b2=bhimUPI("ani",21,"male","5 jan 2009")
# class zomoto:
    

# class customer(swiggy,zomato):
#     def order(self):
#         print("just ordering")
# s1=swiggy("raj",21,"male","2 july 2002")












# class User:
#     def __init__(self, name, age, gender, dob):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.dob = dob

#     def login(self):
#         print("Successfully Logged in")

#     def logout(self):
#         print("Successfully Logged out")

#     def display_user(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Gender:", self.gender)
#         print("DOB:", self.dob)


# # Single Inheritance
# class Instagram(User):
#     def post(self):
#         print(self.name, "posted a photo")
#         print("Got 1L likes")


# a1 = Instagram("Parul", 15, "Male", "23-07-2004")

# a1.login()
# a1.post()
# a1.logout()


# # Restaurant class
# class Restaurant:
#     def __init__(self, restaurant_name, rating, address):
#         self.restaurant_name = restaurant_name
#         self.rating = rating
#         self.address = address

#     def display_menu(self):
#         print("Menu:")
#         print("Chicken Biryani")
#         print("Chicken 65")
#         print("Mutton Biryani")

#     def restaurant_details(self):
#         print("Restaurant:", self.restaurant_name)
#         print("Rating:", self.rating)
#         print("Address:", self.address)


# # Multiple Inheritance
# class Swiggy(User, Restaurant):
#     def __init__(self, name, age, gender, dob,
#                  restaurant_name, rating, address):
        
#         User.__init__(self, name, age, gender, dob)
#         Restaurant.__init__(
#             self,
#             restaurant_name,
#             rating,
#             address
#         )

#     def display(self):
#         print("Swiggy User Details")


# s1 = Swiggy(
#     "Shiva",
#     20,
#     "Male",
#     "1-Jan-2005",
#     "Paradise",
#     4.5,
#     "Hyderabad"
# )

# s1.display()
# s1.display_user()
# s1.restaurant_details()
# s1.display_menu()


# # Bank
# class Bank(User):
#     bank_name = "RBI"

#     def guidelines(self):
#         print("Beware of scammers")
#         print("Never share your OTP")


# class BhimUPI(Bank):
#     def payments(self, amount):
#         print(amount, "has been paid through UPI")


# b1 = BhimUPI(
#     "Nani",
#     21,
#     "Male",
#     "5-Jan-2003"
# )

# b2 = BhimUPI(
#     "Ani",
#     21,
#     "Male",
#     "5-Jan-2009"
# )

# b1.login()
# b1.guidelines()
# b1.payments(500)


# # Another Restaurant App
# class Zomato(User, Restaurant):
#     def __init__(self, name, age, gender, dob,
#                  restaurant_name, rating, address):

#         User.__init__(self, name, age, gender, dob)
#         Restaurant.__init__(
#             self,
#             restaurant_name,
#             rating,
#             address
#         )

#     def order(self):
#         print(self.name, "placed an order through Zomato")


# z1 = Zomato(
#     "Raj",
#     21,
#     "Male",
#     "2-Jul-2002",
#     "Mehfil",
#     4.3,
#     "Hyderabad"
# )

# z1.login()
# z1.order()
# z1.display_menu()


# # Multiple inheritance again
# class Customer(Swiggy, Zomato):
#     def customer_order(self):
#         print(self.name, "is ordering food")


# c1 = Customer(
#     "Kiran",
#     22,
#     "Male",
#     "10-Aug-2004",
#     "Bawarchi",
#     4.4,
#     "Hyderabad"
# )

# c1.login()
# c1.customer_order()


# class a:
#     def sound(self):
#         print("hii")
# class b(a):
#     def sound(self):
#         super().sound()
#         print("shiva")
# class c(a):
#     def sound(self):
#         print("ela unnav..")
# s1=b()
# s1.sound()
# class a:
#     def sound(self):
#         print("hii")
# class b:
#     def sound(self):
#         print("shiva")
# class c(a,b):
#     def sound(self):
#         super().sound()
#         print("ela unnav")
# s1=c()
# s1.sound()



class a:
    def __init__(self,gen):
        self.gen=gen
class b(a):
    def __init__(self,mail,no,gen):
        self.mail=mail
        super().__init__(no,gen)
class c(a):
    def __init__(self,no,gen):
        self.no=no
        super().__init__(gen)
class d(b,c):
    def __init__(self,name,mail,no,gen):
        self.name=name
        super().__init__(mail,no,gen)
    def display(self):
        print(self.name,self.mail,self.no,self.gen)
s1=d("shiva","shiva@gmail.com",12345678,"male")
s1.display()
print(d.mro())

