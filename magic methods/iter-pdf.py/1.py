# Write a custom iterator that prints numbers from 1 to N.

# class num:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<=self.l:
#             value=self.index
#             self.index+=1
#             return value
#         else:
#             raise StopIteration
# a=num(10)
# for i in a:
#     print(i)

       
# Create an iterator that returns only even numbers from a given list.(doubt)------------------

# class even:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.l):
#             value=self.l[self.index]
#             self.index+=1
#             if value%2==0:
#                 return value
#             return self
#         else:
#             raise StopIteration
# a=even([2,3,4,5,6,7,8,9])
# for i in a:
#     # if i is None:
#     #     continue
#     print(i)



#Implement an iterator that iterates over a string character by character in reverse order.

# class string:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             value=self.l[::-1]
#             self.index+=1
#             return value
#         else:
#             raise StopIteration
# a=string("shiva")
# a.__iter__
# print(a.__next__())
# # for i in a:
# #     print(i)


# Write an iterator that yields elements of a list with their index (don’t use enumerate).

# l = ["apple", "banana", "orange"]

# for i, v in enumerate(l):
#     print(i, v)

# class shiva:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             value=(self.index,self.l[self.index])
#             self.index+=1
#             return value
#         else:
#             raise StopIteration
# a=shiva(["banana","apple","orenge"])
# for i in a:
#     print(i)

#Write a generator that yields digits from an integer one by one.

# def digit(n):
#     for i in range(2,n):
#         yield i
# a=digit(100)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

#Create a generator that yields cumulative sum of numbers in a list. Example: [1,2,3] → 1, 3, 6

# def cum(l):
#     total=0
#     for i in l:
#         total=total+i
#         yield total
# a=cum([1,2,3])
# print(next(a))
# print(next(a))
# print(next(a))




# class cum:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             value=self.l[self.index]
#             self.index+=1
#             return value
#         else:
#             raise StopIteration
# a=cum([1,2,3])
# sum=0
# for i in a:
#     sum=sum+i
#     print(sum,end=" ")


#Implement a generator that yields vowels from a string.

# def vowel(l):
#     for i in l:
#         if i in "aeiouAEIOU":
#             yield i
# a=vowel("shiva")
# print(next(a))
# print(next(a))

#Create an iterator that yields words from a sentence one by one.

# def sent(l):
#     for i in l:
#         yield i
# a=sent(["hii how are you")
# print(next(a))
# print(next(a))
# print(next(a))


# class sent:
#     def __init__(self,l):
#         self.l=l.split()
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             value=self.l[self.index]
#             self.index+=1
#             return value #doubt why not yield
# a=sent("hi how are you")
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# l="hi how are you?"
# # for i in l:
# #     print(i)
# it=iter(l)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

class number:
    def __init__(self,n):
        self.n=n
        self.index=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>0:
            value=self.index
            self.index-=1
            return value
        else:
            raise StopIteration
n=int(input())
a=number(n)
for i in a:
    # if i is None:
    #     break
    print(i)