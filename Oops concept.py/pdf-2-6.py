class vehicle:
    service_charge=3
    def __init__(self,model,km):
        self.model=model
        self.km=km
        self.service_history=[]
    def add(self):
        charge=self.km*vehicle.service_charge
        return charge
    def history(self,service):
        self.service_history.append(service)
    @classmethod
    def change(cls,new):
        cls.service_charge=new
    @staticmethod
    def check(aa):
        return aa>15
    def display(self):
        print("model:",self.model)
        print("km:",self.km)
        print("service history:",self.service_history)
        print("calculate service charge:",self.add())
        print("eligibility:",vehicle.check(self.km))
        
        print("_"*12)
a=vehicle("hero",2500)
b=vehicle("pulser",4500)
a.history("engine check")
b.history("break check")
a.display()
b.display()
vehicle.change(5)
print("after change the service charge rate:")
a.display()
b.display()


    
