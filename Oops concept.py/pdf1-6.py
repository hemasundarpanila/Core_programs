# class Book:
#     totalbooks=0
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         Book.totalbooks=Book.totalbooks+1
#     @classmethod
#     def from_string(cls,book_str):
#         title,author=book_str.split("-")
#         return cls(title,author)
#     @staticmethod
#     def is_valid(title):
#         return len(title)>=3
#     def display(self):
#         print("title name:",self.title)
#         print("author name:",self.author)
#         print("verification:",Book.is_valid(self.title))
#         print(Book.totalbooks)
#         print("_"*14)
# a=Book("python","shiva")
# a.display()
# b=Book("java","nani")

# b.display()
# c=Book.from_string("c++-mangala")
# c.display()


class book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        book.total_books+=1
    @classmethod
    def valid_title(cls,bk):
        title,author=bk.split("-")
        return cls(title,author)
    @staticmethod
    def validation(Aa):
        return len(Aa)>3
    def display(self):
        print("title:",self.title)
        print("author",self.author)
        print("validation:",book.validation(self.title))
        print(book.total_books)
        print("_"*12)
title1="python"
if book.validation(title1):
    a1=book(title1,"shiva")
    print("book is valid")
    a1.display()
else:
    print("book is not valid")
# b=book("java","nani")
# b.display()
title2="c++-saiganesh"
book.valid_title(title2)
if book.validation(title2):
    c=book.valid_title(title2)
    print("book is valid")
    c.display()
else:
    print("book is not valid")
#c.display()
    
