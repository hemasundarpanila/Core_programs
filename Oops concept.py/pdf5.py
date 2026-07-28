class Shiva:
    # def __init__(self,celsius):
    #     self.celsius=celsius
    # def convert(self):
    #     print(self.celsius)
    @staticmethod
    def display(celsius):
        print("Fahrenheit:",(celsius*9/5)+32)
a=Shiva()
# a.convert()
a.display(37)