class Employee:
    bonus=0.1
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def finalsalary(self):
        return self.salary+(self.salary*self.bonus)
    @classmethod
    def update(cls,new):
        cls.bonus=new
    @staticmethod
    def valid(sal):
        if sal>=10000:
            print("valid salary")
        else:
            print("not valid")
    def display(self):
        print("employee name:",self.name)
        print("employee salary:",self.salary)
        print("final salary:",self.finalsalary())
        #print("final salary:",b.finalsalary())
        Employee.valid(self.salary)
        print("_"*15)
        
a=Employee("shiva",20000)
b=Employee("nani",1000)
a.display()
b.display()
Employee.update(0.3)
print("after update the bonus:")
a.display()
b.display()


        
        
