class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __len__(self):
        return self.pages  
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f"{self.title} by {self.author}"
book1=Book("Python","Amit",200)
print(repr(book1))
