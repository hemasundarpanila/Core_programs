class Corse:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
    def entroll(self):
        Corse.total_students+=1   
    @classmethod
    def show_total(cls):
        return cls.total_students
    @staticmethod
    def is_eligible(age):
        return age>=18
a=Corse("shiva")
b=Corse("nani")
print(a.student_name)
print(b.student_name)
a.entroll()
b.entroll()
print(Corse.show_total())
print(Corse.is_eligible(20))
print(Corse.is_eligible(12))


        
