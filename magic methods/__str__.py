# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return (f"student name {self.name} and age is {self.age}")
#     def __repr__(self):
#         return ((f"{self.name} and {self.age}"))
# a=student("shiva",21)
# b=student("shiva",21)
# c=student("shiva",21)
# d=[a,b,c]
# print(repr(d))
# print(a)/

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary*12
    def __str__(self):
        return f'name:{self.name}\nsalary:{self.salary}\n'
    def __add__(self, other):
        return Employee("t",self.salary+other.salary)
        # return f'addition of both salaries:{self.salary+other.salary}'
    def __mul__(self, other):
        return f'Multiplication of  both salary :{self.salary*other.salary}'
    def __ne__(self, other):
        if self.salary!=other.salary:
            return f'{self.name} & {other.name} Salaries are not Equal'
        else:
            return f'{self.name} & {other.name} Salaries are Equal'

    def __le__(self, other):
        if self.salary<other.salary:
            return f'{self.name} has Less salary than {other.name}'
        elif self.salary==other.salary:
            return f'{self.name} & {other.name} have equal salaries'
        else:
            return f'{self.name} & {other.name}  salaries are not <= to each other'

e1=Employee('Aadhya',5000)
e2=Employee('paaru',4000)
e3=Employee('shiva',5000)
e4=Employee('shiva',5000)
e5=Employee('shiva',5000)

# print(e1<=e2)
# print(e1!=e2)
# print(e1==e3)
# print(e1*e3)
print(e1+e2+e3+e4+e5)