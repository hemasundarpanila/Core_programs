class book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        book.total_books+=1
    @classmethod
    def from_string(cls,aa):
        title,author=aa.split("-")
        return cls(title,author)
    @staticmethod
    def is_valid(title):
        return len(title)>3
    def display(self):
        print("book name:",self.title)
        print("book author:",self.author)
        print("totak books:",book.total_books)
        print("validation title:",book.is_valid(self.title))
        print("-"*13)
a=book("python","shiva")
a.display()
b=book("java","nani")
b.display()
c=book.from_string("c++-sai")
c.display()
