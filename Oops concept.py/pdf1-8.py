# class Course:
#     total_students=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age 
#     def entrol(self):
#         Course.total_students+=1
#     @classmethod
#     def show(cls):
#         return cls.total_students
#     @staticmethod
#     def check(aa):
#         return aa>=18
#     def display(self):
#         print("student name:",self.name)
#         print("student age:",self.age)
#         print("validation:",Course.check(self.age))
#         self.entrol()
#         print("total students:",Course.show())
#         print("*"*13)
# a=Course("shiva",21)
# b=Course("nani",14)
# a.display()
# b.display()
class course:
    total_students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def enroll(self):
        course.total_students=course.total_students+1
    @classmethod
    def show_total(cls):
        return cls.total_students
    @staticmethod
    def eligible(Aa):
        return Aa>=18
    def display(self):
        print("student name:",self.name)
        print("student age:",self.age)
        self.enroll()
        print("total students:",course.show_total())
        print("eligibility:",course.eligible(self.age))
        print("_"*12)

a=course("shiva",19)
b=course("nani",14)
a.display()
b.display()


