#1.	Write a generator that yields numbers from 1 to N.

# def fun(n):
#     for i in range(1,n+1):
#         yield i
# s=fun(10)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# # for i in s:
# #     print(i)

#2.	Write a generator that yields even numbers from 1 to N
# def fun(n):
#     for i in range(1,(n*2)+1):
#         if i%2==0:
#             yield i
#     #raise StopIteration
# s=fun(5)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# # for i in s:
# #     print(i)

#3.	Write a generator that yields each character of a string.
# def cha(n):
#     for i in range(len(n)-1,-1,-1):
#         yield n[i]
# s=cha("shiva")
# for i in s:
#     print(i)

#5.	Write a generator that yields only vowels from a string.
# def vowel(n):
#     for i in range(1,len(n)):
#         if n[i] in "aeiouAEIOU":
#             yield n[i]
# s=vowel("shiva")
# for i in s:
#     print(i)

#8.	Write a generator that yields digits from an integer one by one.

# def shiva(n):
#     for i in str(n):
#         yield i
# s=shiva("123")
# for i in s:
#     print(i)

#9.	Create a generator that yields cumulative sum of numbers in a list. Example: [1,2,3] → 1, 3, 6
# def fun(n):
#     sum=0
#     for i in n:
#         sum=sum+i
#         yield sum
# s=fun([1,2,3])
# for i in s:
#     print(i)

# def fun(n):
#     sum=0
#     for i in range(len(n)):
#         sum=sum+n[i]
#         yield sum
# t=fun([1,2,3])
# # print(next(t))
# # print(next(t))
# for i in t:
#     print(i)

