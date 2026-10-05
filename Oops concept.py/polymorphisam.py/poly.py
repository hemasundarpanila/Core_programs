# class A:
#     def sound(self):
#         print("hii")
# class B:
#     def sound(self):
#         print("shiva")
# s1=A()
# s1=B()
# s1.sound()
# s1.sound()

# class dog:
#     def sound(self):
#         print("hello")
# class cat:
#     def sound(self):
#         print("shiva")
# # def make_sound(animal):
# #     animal.sound()
# # obj1=dog()
# # obj2=cat()
# # make_sound(obj1)
# # make_sound(obj2)
# animals=[dog(),cat()]
# for animal in animals:
#     animal.sound()

# class student:
#     def __init__(self,marks):
#         self.marks=marks
#     def __str__(self):
#         return f"{self.marks}"
#     def __add__(self,other):
#         return student(self.marks+other.marks)
# s1=student(20)
# s2=student(40)
# s3=student(20)
# print(s1+s2+s3)

# class Test:

#     def add(self, a, b,c=0):
#         return a + b
# class nani:
#     def add(self, a, b, c):
#         return a + b + c
# s1=Test()
# s2=nani()
# print(s1.add(10,20))
# print(s2.add(10,20,30))


# class name:
#     def student(self):
#         print("shiva")
# class age:
#     def student(self):
#         print("my age is 22")
# # def check(value):
# #     value.student()
# # # s=name()
# # s2=age()
# # check(s)
# # check(s2)
# value=[name(),age()]
# for i in value:
#     i.student()

# class student:
#     def __init__(self,marks):
#         self.marks=marks
#     def __str__(self):
#         return f"{self.marks}"
#     def __add__(self,other):
#         return student(self.marks+other.marks)
# s1=student(80)
# s2=student(90)
# s3=student(90)
# s4=student(40)
# print(s1+s2+s3+s4)

# class test:
#     def add(self,a,b,c=0):
#         return a+b+c
# s=test()
# print(s.add(10,10))
class A:
    def test(self):
        print("one")

    def test(self):
        print("two")
s=A()
s.test()