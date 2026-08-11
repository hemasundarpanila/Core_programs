# class A:
#     def __init__(self,x):
#         self.x=x
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.x+=1
#         return self.x
# a=A(30)
# l=iter(a)
# print(next(l))


# class sun:
#     def __init__(self,s,e):
#         self.start=s
#         self.end=e
#     # def __iter__(self):
#     #     return self
#     def __next__(self):
#         if self.start<=self.end:
#             self.start+=1
#             return self.start
#         else:
#             raise StopIteration
# a1=sun(3,7)
# print(next(a1))
# #d=iter(a1)
# print(next(a1))
# print(a1.__next__())
# print(a1.__next__())
# print(a1.__next__())


# class A:
#     def __init__(self, x):
#         self.x = x

#     def __next__(self):
#         self.x += 1
#         return self.x

# a = A(10)

# print(next(a))



# l=["shiva1","shiva2","shiva3","shiva4"]
# it=iter(l)
# it2=l.__iter__()
# print(it,it2,sep='\n')
# print(next(it))
# print(next(it2))
# print(it.__next__())
# print(it.__next__())
# print(it2.__next__())

# class playlist:
#     def __init__(self,l):
#         self.lst=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.lst):
#             song=self.lst[self.index]
#             self.index+=1
#             return song
#         # else:
#         #     raise StopIteration
# p1=playlist(["irumudi","fear","dude"])
# p2=playlist(["hukum","vilram ost","orum blood","RX 100"])
# p=iter(p2) 
# for i in p2:
#     if i is None:
#         break
#     print(i)

#doubt

# class attendence:
#     def __init__(self,st):
#         self.student=st
#         self.roll_no=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.roll_no<len(self.student):
#             name=self.student[self.roll_no]
#             self.roll_no+=1
#             return name
#         else:
#             raise StopIteration
        
# st1=attendence(["adi","sai","shiva","nani"])
# st2=attendence(["adithi","sai sri","shivani","nanilaa"])

# #p=iter(st1)
# for i in (st1):
#     print(f"{i} :  present")
# for j in (st2):
#     print(f"{j} :  present")


# class even:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.l):
#             n=self.l[self.index]
#             self.index+=1
#             if n%2==0:
#                 return n
#         # else:
#         #     return next(self)  
#         raise StopIteration
# e=even([1,2,3,4,5,6,7])
# for i in e:
#     print(i)

# l=[10,20,30,40,50]

# print(next(l))
# print(next(l))
# print(next(l))


# class student:
#     def __init__(self,la):
#         self.la=la
#         self.roll=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.roll<len(self.la):
#             name=self.la[self.roll]
#             self.roll+=1
#             return name
#         #raise StopIteration
# a=student(["shiva","nani","sai","abhi"])
# # p=iter(a)
# # print(next(a))
# # print(next(a))
# # print(next(a))
# for i in a:
#     if i is None:
#         break
#     print(i)


# class even:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             k=self.l[self.index]
#             if k%2==0:
#                 s=s+k
#                 return s

# a=even([1,2,3,4,5,6,7])
# for i in a:
#     if i is None:
#         break
#     print(i)



# l=list(map(int,input().split()))
# n=int(input())
# s=min(l)+1
# c=0
# while(True):
#     if s not in l:
#         print(s)
#         c=c+1
#         if c==n:
#             break
#     s=s+1




# class attendence:
#     def __init__(self,st):
#         self.student=st
#         self.roll_no=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while(self.roll_no<len(self.student)):
#             self.roll_no+=1
#             name=self.student[self.roll_no-1]
#             if name not in "aeiouAEIOU ":
#                 return name
#             else:
#                 continue        
#         else:
#             raise StopIteration
        
# st1=attendence("who are you")
# st2=attendence(["adithi","sai sri","shivani","nanilaa"])

# for j in (st1):
#     # if j is None:
#     #     break
#     print(f"{j}")

# class shi:
#     def _init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while (self.index<len(self.l)):
#             value=int(self.l[self.index])
#             self.index+=1
#             if value%2==0:
#                 return value
#         raise StopIteration
# a1=shi([2,3,4,5,6,7,8])
# for i in a1:
#     print(i,end=" ")


# a=int(input())
# b=int(input())
# l=min(a,b)
# for i in range(l,0,-1):
#     if a%i==0 and b%i==0:
#         print(i)
#         break

