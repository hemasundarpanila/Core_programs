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

# # class InsufficientBalanceError(Exception):
# #     pass
# # balance = 5000
# try:
#     balance=5000
#     amount = int(input("Enter withdrawal amount: "))
#     if amount <= 0:
#         raise ValueError("Amount must be positive")
#     if amount > balance:
#         raise ValueError("Insufficient balance")
#     balance = balance - amount
# except ValueError as e:
#     print("Invalid amount:", e)
# except ValueError as e:
#     print("Transaction failed:", e)
# else:
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)
# finally:
#     print("Thank you")



# def fun(n):
#     for i in range(n):
#         return i
# a=fun(10)
# print(a)

# l=[1,2,3,1]
# s=set()
# for i in l:
#     if i not in s:
#         s.add(i)
#     else:
#         print("true")
# print("flase0")

# try:
#     a=int(input())
#     b=int(input())
#     raise ValueError()
#     c=a/b
#     print(c)
# except ValueError as e:
#     print("error occurd")
# except Exception as e:
#     print("something")
# else:
#     print("division is calculated")
# finally:
#     print("finished")