# class Student:
#     def check(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def passed(self):
#         return self.marks>40
# a=Student()
# a.check("shiva",30)
# b=Student()
# b.check("nani",60)
# print(a.name,a.marks,a.passed())
# print(b.name,b.marks,b.passed())


        
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def passed(self):
#         if self.marks>40:
#             return "passed"
#         else:
#             return "fail"
# a=Student("sai",95)
# b=Student("shiva",30)
# print(a.name,a.marks,a.passed())
# print(b.name,b.marks,b.passed())


# class book:
#     total_books=0
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         book.total_books+=1
#     @classmethod
#     def from_string(cls,book_str):
#         title,author=book_str.split("-")
#         return cls(title,author)
#     @staticmethod
#     def valid(title):
#         if len(title)>3:
#             print("valid")
#         else:
#             print("not valid")
#     def display(self):
#         print("book title:",self.title)
#         print("book author:",self.author)
#         book.valid(self.title)
#         print("total books:",book.total_books)
#         print("-"*13)
# a=book("python","shiva")
# a.display()
# b=book.from_string("java-nani")
# b.display()

# l="hello worl8d"
# k=[]
# h=[]
# for i in l:
#     if i in "aeiouAEIOU":
#         k.append(i)
#     else:
#         if i.isalpha():
#             h.append(i)
# print("vowels:",len(k))
# print("consonents:",len(h))

# l=[2,4,5,1]
# k=l[0]+1
# c=0
# while(k>0):
#     if k not in l:
#         print(k)
#         c=c+1
#         if c==4:
#             break
#     k=k+1

# l="hello"
# for i in range(len(l)-1,-1,-1):
#     print(l[i],end="")

l=[0,1,0,2,3,0,0,4,5]
for i in l:
    if i==0:
        l.append(l.pop(i))
print(l)