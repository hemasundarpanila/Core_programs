# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         print("hello")
#     def shiva(self):
#         print("hii")
# class upi(payment):
#     def pay(self,amount):
#         super().pay()
#         print("using upi:",amount)
# class card(payment):
#     def pay(self,amount):
#         print("using card:",amount)
# u=upi()
# c=card()
# u.pay(100)
# c.pay(200)
# print(card.mro())

# from abc import ABC,abstractmethod
# class user(ABC):
#     @abstractmethod
#     def pay(self):
#         print("hii")
#     def shiva(self):
#         print("hello")
# class upi(user):
#     @abstractmethod
#     def pay(self):
#         print("upi")
# class card(upi):
#     def pay(self):
#         print("card")
# u=upi()
# c=card()
# u.pay()
# c.pay()
     

# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
# class UPI(Payment):
#     def pay(self, amount):
#         print("UPI PIN checking...")
#         print("Bank account checking...")
#         print("Payment processing...")
#         print("₹", amount, "paid using UPI")
# class Card(Payment):
#     def pay(self, amount):
#         print("Card number checking...")
#         print("CVV checking...")
#         print("Bank verification...")
#         print("₹", amount, "paid using Card")
# def make_payment(payment_method, amount):
#     payment_method.pay(amount)

# upi = UPI()
# make_payment(upi, 500)

n=int(input())
for i in range(n):
    if i<=5:
        print("hii")
    else:
        print("hello")