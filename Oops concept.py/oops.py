class Student:
    def check(self,name,marks):
        self.name=name
        self.marks=marks
    def passed(self):
        return self.marks>40
a=Student()
a.check("shiva",30)
b=Student()
b.check("nani",60)
print(a.name,a.marks,a.passed())
print(b.name,b.marks,b.passed())


        
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def passed(self):
        if self.marks>40:
            return "passed"
        else:
            return "fail"
a=Student("sai",95)
b=Student("shiva",30)
print(a.name,a.marks,a.passed())
print(b.name,b.marks,b.passed())
