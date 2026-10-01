# class Employee:
#     bonus=0.1
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def finalsalary(self):
#         return self.salary+(self.salary*self.bonus)
#     @classmethod
#     def update(cls,new):
#         cls.bonus=new
#     @staticmethod
#     def valid(sal):
#         if sal>=10000:
#             print("valid salary")
#         else:
#             print("not valid")
#     def display(self):
#         print("employee name:",self.name)
#         print("employee salary:",self.salary)
#         print("final salary:",self.finalsalary())
#         #print("final salary:",b.finalsalary())
#         Employee.valid(self.salary)
#         print("_"*15)
        
# a=Employee("shiva",20000)
# b=Employee("nani",1000)
# a.display()
# b.display()
# Employee.update(0.3)
# print("after update the bonus:")
# a.display()
# b.display()


class emp:
    bonus=0.1
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def final_sal(self):
        self.sal=self.sal+(self.sal*emp.bonus)
        return self.sal
    @classmethod
    def update_bonus(cls,new):
        cls.bonus=new
    @staticmethod
    def is_valid(check):
        if check>0:
            return "valid"
        else:
            return "not valid"
    def display(self):
        print("employee name:",self.name)
        print("employee salary:",self.sal)
        print("with bonus:",self.final_sal())
        print("validation:",emp.is_valid(self.sal))
        print("-"*12)
s1=emp("shiva",10000)
s2=emp("nani",20000)
s1.display()
s2.display()
emp.update_bonus(0.4)
print("after update the bonus:")
s1.display()
s2.display()
        
        
