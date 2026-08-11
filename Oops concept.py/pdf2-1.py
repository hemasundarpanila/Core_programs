class Student:
    total_std=0
    pass_mark=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_std+=1
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
    def grade(mark):
        if mark>90:
            return "A"
        elif  90> mark >=70:
            return "B"
        elif 70> mark >=50:
            return "c"
        elif 40<=mark<=49:
            return "D"
        else:
            return "No Grade"
    def display(self):
        print("student name:",self.name)
        print("studnet marks",self.marks)
        print("student certificate:",self.check())
        print("student certificate:",Student.grade(self.marks))
        print("total students:",Student.total_std)
        print("-"*15)

a=Student("shiva",30)
a.display()
b=Student("nani",50)
b.display()
c=Student("sai",80)
c.display()
# print(a.name,a.marks)
# print(b.name,b.marks)
# print(c.name,c.marks)
students=[a,b,c]
Student.increse(students,50)
# print(a.check(),b.check(),c.check())
# print(a.grade(a.marks))
# print(b.grade(b.marks))
# print(c.grade(c.marks))
print("after increse marks:-----")
a.display()
b.display()
c.display()

        
