class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        return self.base_salary+(self.base_salary*self.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal>0
a=Employee("shiva",50000)
b=Employee("nani",40000)
print(a.final_salary())
print(b.final_salary())
Employee.update_bonus(0.2)
print(a.final_salary())
print(b.final_salary())
print(a.is_valid_salary(500000))
print(b.is_valid_salary(-900))

