class Employee:
    companyname="techcorp"
    def show(self):
        print("my company name is:",self.companyname)
    @classmethod
    def changecompany_name(self,newname):
        self.companyname=newname
a=Employee()
a.show()
a.changecompany_name("apple")
a.show()
b=Employee()
b.show()
