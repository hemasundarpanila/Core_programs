class employee:
    experience=5
    def __init__(self,name,ex,dept):
        self.name=name
        self.ex=ex
        self.dept=dept
    def eligible(self):
        if self.ex>=employee.experience:
            return "eligible"
        else:
            return "not eligible"
    @classmethod
    def update(cls,new):
        cls.experience=new
    @staticmethod
    def check(AA):
        DE=["HR","Tech","Admin"]
        if AA in DE:
            print("valid deprt")
        else:
            print("not valid")
    def display(self):
        print("employee name:",self.name)
        print("employee experience:",self.ex)
        print("employee department:",self.dept)
        employee.check(self.dept)
        print(self.eligible())
        print("-"*13)
a=employee("shiva",6,"HR")
b=employee("nani",3,"Teacher")
a.display()
b.display()
employee.update(2)
print("after update the experience:")
a.display()
b.display()

