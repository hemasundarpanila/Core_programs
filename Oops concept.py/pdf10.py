class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>self.passing_marks:
            print("pass")
        else:
            print("fail")
    @classmethod
    def updating(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade(marks):
        if marks>90:
            return "A"
        elif marks>70:
            return "B"
        else:
            return "C"
a=Student("shiva",30)
b=Student("nani",95)
print(a.name,a.marks)
print(b.name,b.marks)
a.updating(20)
a.result()
b.result()
print(Student.grade(a.marks))
print(Student.grade(b.marks))
    
