'''Write a function named find_length(obj) that uses a loop to calculate the 
length of the given object without using the built-in len() function. The 
function should return the calculated length if the object is iterable. If a 
non-iterable object such as an integer is passed, the function should raise and 
handle a TypeError, and print an appropriate error message explaining what 
happens when an integer is sent as input.
'''

# def find_length(obj):
#     try:
#         c=0
#         for i in obj:
#             c=c+1
#         return c
#     except TypeError:
#         print("given value not iterable")
# print(find_length("hello"))
# print(find_length(100))

# class person:
#     def __init__(self,age):
#         self.age=age
#         try:
#             if age<0:
#                 raise ValueError("age must positive")
#             return age
#         except ValueError as e:
#             print(e)
# s=person(3)
# print(s.age)

# class person:
#     def __init__(self, age):
#         self.age=age
#         try:
#             if age < 0:
#                 raise ValueError("Age must be greater than or equal to 0")
#             return self.age
#         except ValueError as e:
#             print(e)
# s = person(-2)
# print(s.age)



# class person:
#     def __init__(self, age):
#         self.age = age
#         try:
#             if age < 0:
#                 raise ValueError("age must be positive")
#             return self.age
#         except ValueError as e:
#             print(e)
# s = person(-22)
# print(s)

# class person:
#     def __init__(self, age):
#         try:
#             if age < 0:
#                 raise ValueError("age must be positive")

#             self.age = age

#         except ValueError as e:
#             print(e)


# s = person(-22)

# if hasattr(s, "age"):
#     print(s.age)

class student:
    marks=0
    def __init__(self,marks):
        pass
    def set_marks(self,marks):
        try:
            if self.marks<0 or 100<self.marks:
                raise ValueError("value must 0 to 100 between")
            self.marks=marks
        except ValueError as e:
            print(e)
s=student(200)
print(s.marks)




