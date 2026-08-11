class book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def reading(self):
        total_time=self.pages*2
        return total_time
    def __str__(self):
        return f"book name:{self.title}\nbook author:{self.author}\nbook pages:{self.pages}"
        
    def __add__(self,others):
        return self.pages+others.pages
    def __floordiv__(self,other):
        return self.pages//other.pages
    def __gt__(self,other):
        return self.pages>other.pages
a=book("python","shiva",90)
b=book("java","nani",30)
print(a)
print(f"total time:{a.reading()} minutes")
print("-"*13)
print(b)
print(f"total time:{b.reading()} minutes")
print("condition details:")
print("-"*13)
print("add two books:",a+b)
print("floor div:",a//b)
print("grater condition:",a>b)
