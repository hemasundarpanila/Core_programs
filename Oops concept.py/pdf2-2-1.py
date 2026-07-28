class student:
    target=40
    total_students=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        #student.total_students+=1
    def update(self):
        self.marks=self.marks+(self.marks*35/100)
    def passing(self):
        if self.marks>=student.target:
            print("pass")
        else:
            print("fail")
    @classmethod
    def change(cls,new):
        cls.target=new
    @staticmethod
    def check(Aa):
        if Aa>=90:
            print("grade A")
        elif Aa>=70:

            print("grade B")
        elif Aa>=50:
            print("grade C")
        else:
            print("grade D")
    def display(self):
        print("student name:",self.name)
        print("student marks:",self.marks)
        student.check(self.marks)
        print("-"*12)
        
a=student("shiva",30)
b=student("nani",60)
a.display()
b.display()
a.passing()
b.passing()
a.update()
b.update()
print("after update the marks:")
a.display()
b.display()
a.passing()
b.passing()


        
