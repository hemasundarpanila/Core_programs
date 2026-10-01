# Create a base class Animal with a method sound(). Create a derived class Dog 
# that overrides the sound() method. Demonstrate method overriding.

# class animal:
#     def sound(self):
#         print("all animals")
# class dog(animal):
#     def sound(self):
#         print("dog is there")
# s1=dog()
# s2=animal()
# s2.sound()
# s1.sound()

#  Create class A with method show(). Create class B(A) that overrides show() and 
# also calls the parent method using super().

# class A:
#     def show(self):
#         print("welcome")
# class B(A):
#     def show(self):
#         print("happy new year")
#         super().show()
# s1=B()
# s1.show()


#Create multi-level inheritance with classes A → B → C, each having a method 
# display() printing the class name. Create object of C and call display(), 
# showing method resolution.

# class A:
#     def display(self):
#         print("class A")
# class B(A):
#     def display(self):
#         print("class B")
# class C(B):
#     def display(self):
#         print("class C")
# s1=C()
# s1.display()
# print(C.mro())


# Implement hierarchical inheritance using a base class Vehicle and two child 
# classes Car and Bike, each defining a method wheels()

# class vehicle:
#     def show(self):
#         print("all vehicles are available")
# class car(vehicle):
#     def wheels(self):
#         print(" 4 wheels vehicles")
# class bike(vehicle):
#     def wheels(self):
#         print(" 2 wheels vehicles")
# s1=bike()
# s1.show()
# s1.wheels()
# print("-"*14)
# s2=car()
# s2.show()
# s2.wheels()

#  Create class Employee with an instance method salary(). Create class 
# Manager(Employee) that overrides salary() and adds an incentive. Demonstrate 
# both outputs.

# class employee:
#     def salary(self):
#         print("employee salary:30000")
# class manager:
#     def salary(self):
#         print("manager salary:50000")
#         print("manager incentive salary:10000")
# s1=manager()
# s1.salary() 
# s2=employee()
# s2.salary()      

#  Create class University with a class variable and a class method. Inherit it 
# into class College and access the parent’s class variable from the child class.

# class university:
#     total_students=5000
#     @classmethod
#     def student(cls,new):
#         cls.total_students=new
# class college(university):
#     def info(self):
#         print(f"total students:{university.total_students}")
# s1=college()
# s1.info()
# university.student(5500)
# s1.info()

# class University:
#     university_name = "JNTU"   # class variable

#     @classmethod
#     def show_university(cls):
#         print("University:", cls.university_name)


# class College(University):
#     pass


# c = College()

# print(c.university_name)
# c.show_university()


# Create class MathOps with a static method add(a, b). Create class 
# AdvancedOps(MathOps) and use the static method without overriding it.

# class mathops:
#     @staticmethod
#     def add(a,b):
#         return a+b
# class advs(mathops):
#     @staticmethod
#     def add(a,b):
#         return a+b
# s1=advs()
# print(advs.add(10,20))
# s2=mathops()
# print(mathops.add(100,20))

# class MathOps:
#     @staticmethod
#     def add(a, b):
#         return a + b
# class AdvancedOps(MathOps):
#     pass
# result = AdvancedOps.add(10, 20)

# print(result)

#  Create two classes Father and Mother, both defining a method skills(). Create 
# class Child(Father, Mother) and check which skills() runs using MRO.

# class father:
#     def skill(self):
#         print("work well")
#         super().skill()
# class mother:
#     def skill(self):
#         print("cook well")  
# class child(father,mother):
#     def skill(self):
#         print("study well")
#         super().skill()
# s1=child()
# s1.skill()
# print(child.mro())

# Create class Person with a constructor __init__(name). Create class 
# Student(Person) with constructor __init__(name, roll). Use super() to call the 
# parent constructor

# class person:
#     def __init__(self,name):
#         self.name=name
# class student(person):
#     def __init__(self,name,roll):
#         self.roll=roll
#         super().__init__(name)
# s1=student("shiva",21)
# print(s1.name)
# print(s1.roll)


# class vehicle:
#     def wheels(self):
#         print("all vehicles")
# class car(vehicle):
#     def wheels(self):
#         super().wheels()
#         print("car has 4 wheels")
# class bike(vehicle):
#     def wheels(self):
#         super().wheels()
#         print("bike has 2 wheels")
# s1=bike()
# s2=car()
# s1.wheels()
# print("-"*12)
# s2.wheels()


# class father:
#     def skill(self):
#         print("work well")
#         super().skill()
# class mother:
#     def skill(self):
#         print("cook well")
# class child(father,mother):
#     def skill(self):
#         super().skill()
#         print("both are well")
# s1=child()
# s1.skill()
# print(child.mro())

# class person:
#     def __init__(self,name):
#         self.name=name
#         print(self.name)
# class student(person):
#     def __init__(self,name,roll):
#         self.roll=roll
#         super().__init__(name)
#         print(self.roll)
#     # def display(self):
#     #     print(self.name,self.roll)
# s1=student("shiva",25)