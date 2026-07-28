class Temp:
    def __init__(self,celsius):
        self.celsius=celsius
    @staticmethod
    def dell(cel):
        return (cel*9/5)+32
    def display(self):
        print("celsius value:",self.celsius)
        print("foren value:",Temp.dell(self.celsius))
        print("_"*15)
a=Temp(37)
b=Temp(40)
a.display()
b.display()
        
