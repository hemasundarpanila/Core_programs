# try:
#     a=int(input("enter:"))
#     b=int(input("enter:"))
#     print(a/b)
# except ValueError:
#     print("something went wrong")
# except ZeroDivisionError:
#     print("division")

# age=int(input("enter:"))
# if age<0:
#     raise ZeroDivisionError("invalid value")
# print("age:",age)

# class InsufficientBalanceError(Exception):
#     pass
# balance = 1000
# amount = 1500
# if amount < balance:
#     raise InsufficientBalanceError("Insufficient balance")
# else:
#     print("hii")

# class InsufficientBalanceError(Exception):
#     pass
# balance = 5000
# try:
#     amount = int(input("Enter withdrawal amount: "))
#     if amount <= 0:
#         raise ValueError("Amount must be positive")
#     if amount > balance:
#         raise InsufficientBalanceError("Insufficient balance")
#     balance = balance - amount
# except ValueError as e:
#     print("Invalid amount:", e)
# except InsufficientBalanceError as e:
#     print("Transaction failed:", e)
# else:
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)
# finally:
#     print("Thank you")


from abc import ABC,abstractmethod
class payment(ABC):
    def __init_(self,balance):
        
