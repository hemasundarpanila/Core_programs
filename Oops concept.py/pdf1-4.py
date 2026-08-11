# class Car:
#     wheels=4
#     def __init__(self,mileage):
#         self.mileage=mileage
#     def display(self):
#         print("car mileage:",self.mileage)
#         print("car wheels:",self.wheels)
#         print("_"*15)
#     @classmethod
#     def change(cls,new):
#         cls.wheels=new
# a=Car(20)
# b=Car(40)
# a.display()
# b.display()
# Car.change(6)
# a.display()
# b.display()



class car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    @classmethod
    def change(cls,new):
        cls.wheels=new
    def display(self):
        print("mileage:",self.mileage)
        print("wheels:",car.wheels)
        print("_"*12)
a=car(40)
a.display()
print("after update wheels:")
car.change(6)
a.display()