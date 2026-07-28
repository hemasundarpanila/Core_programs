class Book:
    totalbooks=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.totalbooks=Book.totalbooks+1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        return cls(title,author)
    @staticmethod
    def is_valid(title):
        return len(title)>=3
    def display(self):
        print("title name:",self.title)
        print("author name:",self.author)
        print("verification:",Book.is_valid(self.title))
        print(Book.totalbooks)
        print("_"*14)
a=Book("python","shiva")
a.display()
b=Book("java","nani")

b.display()
c=Book.from_string("c++-mangala")
c.display()

