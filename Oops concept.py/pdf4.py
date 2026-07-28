class car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display(self):
        print("Mileage:",self.mileage)
        print("Wheels:",self.wheels)
    @classmethod
    def shiva(cls,new):
        cls.wheels=new
a=car(20)
a.display()
car.shiva(6)
a.display()
