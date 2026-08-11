# x=9
# def fun():
#     def inner():
#         print(x)
#     return inner
# a=fun()
# a()





# def fun():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         print(count)
#     return inner
# a=fun()
# a()
# a()


# def shopping_cart(item_name):
#     def inner(quantity,price):
#         totalprice=quantity*price
#         print("item name:",item_name)
#         print("quantity:",quantity)
#         print("total price:",totalprice)
#     return inner
# a=shopping_cart("biscuit")
# a(2,200)



# def fun(pass1):
#     def inner(pass2):
#         if pass1==pass2:
#             print("Access Granted")
#         else:
#             print("Access denied")
#     return inner
# a=fun(1234)
# b=fun("sai")
# b("sai")
# a(1239)


# def fun(item):
#     def inner(quantity):
#         print(f"{item} packed {quantity} parcels")
#     return inner
# a=fun("Biriyani")
# a(2)              




# def fun(number):
#     def inner(number2):
#         return number*number2
#     return inner 
# a=fun(10)
# print(a(20))



# Question 5

# Write a function movie(movie_name).

# -   The outer function stores the movie name.
# -   The inner function receives the person’s name.
# -   Print that the person booked a ticket for the movie.
# -   Return the inner function.



# def fun(movie):
#     def inner(name):
#         print(f"{name} booked a ticket for the {movie}")
#     return inner
# a=fun("adipurush")
# b=fun("salaar")
# a("prabhash")
# b("sai ganesh")




# Question 4

# Write a function bank_account(balance).

# -   The outer function receives the initial balance.
# -   The inner function receives an amount to withdraw.
# -   Print the remaining balance.
# -   Return the inner function.

# ------------------------------------------------------------------------


# def fun(balance):
#     def inner(aa):
#         total=balance-aa
#         print("remaining balance",total)
#     return inner
# a=fun(100000)
# a(500)




# Question 3

# Write a function discount(percent).

# -   The outer function receives the discount percentage.
# -   The inner function receives the product price.
# -   Print the final price after applying the discount.
# -   Return the inner function.



# def fun(percent):
#     def inner(price):
#         discount=(price*percent/100)
#         total=price-discount
#         print("total price:",total)
#     return inner
# a=fun(20)
# a(1500)
# a(2300)



# Question 2

# Write a function salarydef(bonus).

# -   The outer function receives the bonus amount.
# -   The inner function receives the employee’s basic salary.
# -   Print the total salary after adding the bonus.
# -   Return the inner function.

# ------------------------------------------------------------------------



# def fun(bonus):
#     def inner(salary):
#         #nonlocal total
#         total=salary+bonus
#         print("total salary:",total)
#     return inner
# a=fun(2000)
# a(30000)
# a(40000)






# Question 1

# Write a function electricity(rate_per_unit).

# -   The outer function receives the cost per unit.
# -   The inner function receives the number of units consumed.
# -   Print the total electricity bill.
# -   Return the inner function.


# def electrycity(rate_per_unit):
#     def inner(units):
#         total=rate_per_unit*units
#         print("electrycity bill:",total)
#     return inner
# a=electrycity(5)
# a(100)
# a(200)