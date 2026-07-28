class Employee:
    company_name="techcorp"
    def show(self):
        print("Company name is:",self.company_name)
    # @classmethod
    def changename(cls,new_name):
        cls.company_name=new_name
a=Employee()
a.changename("newcorp")
a.show()
b=Employee()
b.show()