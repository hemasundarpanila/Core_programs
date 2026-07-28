class Book:
    totalbooks=0
    def __init__(self,title,author):#shiva-train
        self.title=title
        self.author=author
        Book.totalbooks+=1
    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        return cls(title,author)
    @staticmethod
    def is_valid_title(title):
        return len(title)>=3
if Book.is_valid_title("java"):
    a1=Book("java","james")
if Book.is_valid_title("to"):
    b1=Book("to","sai")
if Book.is_valid_title("python"):
    c1=Book.from_string("python-gueo")
print(a1.title,a1.author)
print(c1.title,c1.author)
print(Book.totalbooks)
        
    
        
        
        
