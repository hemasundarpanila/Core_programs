class Employee:
    experience_rate=5
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def eli(self):
        if self.experience>=self.experience_rate:
            return "eligible"
        else:
            return "not eligible"
    @classmethod
    def update(cls,new):
        cls.experience_rate=new
    @staticmethod
    def check(department):
        s=["HR","Tech","Admin"]
        if department in s:
            return "valid"
        else:
            return "not valid"
    def display(self):
        print("employee name:",self.name)
        print("employee experience:",self.experience)
        print("employee department:",self.department)
        print("eligibility:",self.eli())
        print("validation:",Employee.check(self.department))
        print("__"*20)
a=Employee("shiva",6,"HR")
b=Employee("nani",8,"Tech")
Employee.update(9)
print("after add experience:",Employee.experience_rate)
a.display()
b.display()
print(Employee.check(b.department))

