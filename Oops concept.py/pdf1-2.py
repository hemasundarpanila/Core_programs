class Employee:
    company_name="techcorp"
    def __init__(self,name,company_name):
        self.name=name
        self.companyname=company_name
    @classmethod
    def change(cls,new):
        cls.company_name=new
    def display(self):
        print("employee:",self.name)
        print("company name:",self.company_name)
        print("-"*15)
a=Employee("shiva","techcorp")
b=Employee("nani","techcorp")
print("before changing company")
a.display()
b.display()
Employee.change("apple")
print("after changing company")
a.display()
b.display()
