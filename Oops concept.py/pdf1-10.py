class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=Student.passing_marks:
            print("pass")
        else:
            print("fail")
    @classmethod
    def update(cls,new):
        cls.passing_marks=new
    @staticmethod

    def grade(mar):
        if mar>=90:
            return "A"
        elif mar>=60:
            return "B"
        elif mar>=30:
            return "C"
        else:
            print("fail")
    def display(self):
        print("student name:",self.name)
        print("student name:",self.marks)
        print("grade:",Student.grade(self.marks))
        print("_"*12)
            
a=Student("shiva",30)
b=Student("nani",60)
a.display()
a.result()
b.display()
b.result()
Student.update(20)
print("after update the marks")
a.display()
a.result()
b.display()
b.result()


