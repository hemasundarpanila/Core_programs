class Course:
    total_students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age 
    def entrol(self):
        Course.total_students+=1
    @classmethod
    def show(cls):
        return cls.total_students
    @staticmethod
    def check(aa):
        return aa>=18
    def display(self):
        print("student name:",self.name)
        print("student age:",self.age)
        print("validation:",Course.check(self.age))
        self.entrol()
        print("total students:",Course.show())
        print("*"*13)
a=Course("shiva",21)
b=Course("nani",14)
a.display()
b.display()

