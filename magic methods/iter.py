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

#2.	Create an custom iterator that prints numbers from N to 1.

# class A:
#     def __init__(self,n):
#         self.n=n
#         self.index=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<self.n:
#             value=self.index
#             self.index+=1
#             return value
#         else:
#             raise StopIteration
# s=A(5)
# for i in s:
#     print(i)
    # c=c+1
    # if c==5:
    #     break

#3.	Create an custom iterator that prints the first N even numbers.
#4.	Create an custom iterator that prints the first N odd numbers.


# class even:
#     def __init__(self,n):
#         self.n=n
#         self.num=1
#         self.c=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.c<=self.n:
#             value=self.num
#             self.num+=1
#             if value%2==1:
#                 self.c+=1
#                 return value
#         else:
#             raise StopIteration
# d=even(10)
# # print(next(d))
# # print(next(d))
# # print(next(d))
# for i in d:
#     print(i)

# class odd:
#     def __init__(self,n):
#         self.n=n
#         self.num=1
#         self.c=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while(self.c<=self.n):
#             value=self.num
#             self.num+=1
#             if value%2==1:
#                 self.c+=1
#                 return value
#         else:
#             raise StopIteration
# s=odd(5)
# for i in s:
#     print(i)


#5.	Create an custom iterator that returns only even numbers from a given list.

# class even:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.n):
#             value=self.n[self.index]
#             self.index+=1
#             if value%2==0:
#                 return value
#         else:
#             raise StopIteration
# s=even([2,3,4,5,6,7])
# for i in s:
#     # if i is None:
#     #     break
#     print(i)

# class odd:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while(self.index<len(self.n)):
#             value=self.n[self.index]
#             self.index+=1
#             if value%2==1:
#                 return value
#         else:
#             raise StopIteration
# d=odd([2,3,4,5,6,7,8])
# for i in d:
#     print(i)

#8.	Create an custom iterator that prints each character of a string one by one.
# class cha:
#     def __init__(self,n):
#         self.n=n
#         k=len(n)-1
#         self.index=k
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while(self.index<len(self.n)):
#             value=self.n[self.index]
#             self.index-=1
#             return value
#         else:
#             raise StopIteration
# s=cha("shiva")
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# # for i in s:
# #     print(i)

# class honey:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while(self.index<len(self.n)):
#             value=self.n[self.index]
#             self.index+=1
#             if value in "aeiouAEIOU":
#                 return value
#         else:
#             raise StopIteration
# s=honey("shiva")
# for i in s:
#     print(i)

# class cal:
#     def __init__(self,n):
#         self.n=n
#         self.c=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while(self.c<=10):
#             h=self.n*self.c
#             self.c+=1
#             return f"{self.n} * {self.c} = {h}"
#         else:
#             raise StopIteration
# s=cal(6)
# for i in s:
#     print(i)

# class prime:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.a<self.b:
#             i=self.a
#             self.a+=1
#             c=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     c=c+1
#             if c==2:
#                 return i
#         else:
#             raise StopIteration
# s1=prime(10,20)
# for i in s1:
#     print(i)

# class num:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.index=self.a
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<=self.b:
#             value=self.index
#             self.index+=1
#             if value%2==0:
#                 return value
#         else:
#             raise StopIteration
# s1=num(10,20)
# for i in s1:
#     print(i)

# class string:
#     def __init__(self,a):
#         self.a=a
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.a):
#             value=self.a[self.index]
#             self.index+=1
#             if value>0:
#                 return value
#         else:
#             raise StopIteration
# s1=string([1,-2,3,4,-5,6])
# for i in s1:
#     print(i)
