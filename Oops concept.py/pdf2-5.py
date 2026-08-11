class course:
    duration_time=30
    total_students=0
    def __init__(self,title,duration):
        self.title=title
        self.duration=duration
        self.student=[]
    def enroll(self,man):
        self.student.append(man)
        course.total_students+=1
    @classmethod
    def change(cls,new):
        cls.duration_time=new
    @staticmethod
    def check(aa):
        return aa>0
    def display(self):
        print("course name:",self.title)
        print("course duration:",self.duration)
        print(self.student)
        print("total students:",self.total_students)
        print(course.check(self.duration))
        print("-"*12)
        pass
a=course("python",40)
b=course("java",50)
a.enroll("shiva")
a.enroll("shiva")
a.enroll("shiva")
b.enroll("nani")
b.enroll("nani")
b.enroll("nani")
a.display()
b.display()
course.change(50)
a.display()
b.display()


