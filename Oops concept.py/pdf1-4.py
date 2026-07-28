class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display(self):
        print("car mileage:",self.mileage)
        print("car wheels:",self.wheels)
        print("_"*15)
    @classmethod
    def change(cls,new):
        cls.wheels=new
a=Car(20)
b=Car(40)
a.display()
b.display()
Car.change(6)
a.display()
b.display()

