class Student:
    total_std=0
    pass_mark=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def check(self):
        if self.marks>=Student.pass_mark:
            return "pass"
        else:
            return "fail"
    @classmethod
    def increse(cls,students,percentage):
        for i in students:
            i.marks+=i.marks*(percentage/100)
    @staticmethod
    def grade(marks):
        if marks>90:
            return "A"
        elif  90> marks >=70:
            return "B"
        elif 70> marks >=50:
            return "c"
        elif 40<=marks<=49:
            return "D"
        else:
            return "No Grade"

a=Student("shiva",30)
b=Student("nani",50)
c=Student("sai",80)
print(a.name,a.marks)
print(b.name,b.marks)
print(c.name,c.marks)
students=[a,b,c]
Student.increse(students,50)
print(a.check(),b.check(),c.check())
print(a.grade(a.marks))
print(b.grade(b.marks))
print(c.grade(c.marks))
print(a.marks)

        
