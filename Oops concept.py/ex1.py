class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):#idi instace method enduku ante ee fuction object data ni use chestundi
        print(self.name)
        print(self.marks)
a=student("shiva",60)
a.display()
b=student("nani",90)
b.display()
