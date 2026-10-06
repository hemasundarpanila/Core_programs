# from functools import reduce
# def cal(*a,op):
#     def add():
#         return reduce(lambda x,y:x+y,*a)
#     def sub():
#         return reduce(lambda x,y:x-y,*a)
#     if op=="+":
#         return add()
#     if op=="-":
#         return sub()
# c=input("operation:")
# print(cal((1,2,3,4),op=c))
    
    




'''def cal(fun,*v1):
    return fun(*v1)
def add():
    return x+y
def sub():
    return x-y
def mul():
    return x*y
print(cal(add,10,20,30,40))'''""
# from functools import reduce
# def add(*args):
#     #print(reduce(lambda x,y:x+y,args))
#     total=0
#     for i in args:
#         total+=i
#     print(total)
# add(1,2,3,4,5)

# def shiva(**kwargs):
#     for key,value in kwargs.items():

#         print(f"{key}:{value}")
# shiva(name="gouda",age=22,college="avanthi")

# def full_example(a,b,*args,option="shiva",**kwargs): 
#     print(a, b, args, option, kwargs) 
 
# full_example(1, 2, 3, 4, 5, option="custom", x=10, y=20) 


# add=lambda x,y:x+y
# print(add(5,6))


# l=lambda x,y:x if x>y else y
# print(l(20,30))


# def shiva(*args):
#     total=0
#     for i in args:
#         total+=i
#     print(total)
# shiva(1,2,3,4,5)
# def shiva(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# shiva(name="shiva",age=22,college="avanthi")

# def shiva(n):
#     result=lambda x:x
#     print(result(n))
# shiva(5678)

# def shiva(n):
#     print(n)
# shiva(5678)

# def fun(n):
#     print("shiva")
#     return n*n
# def fun2(fun,value):
#     print("hii")
#     return fun(value)
# x=fun2(fun,12)
# print(x)

# def shiva(n):
#     return n
# def nani(fun,value):
#     return shiva(value)
# x=nani(shiva,21)
# print(x)

# num=[1,2,3,4]
# def shiva(x):
#     return x*2
# result=list(map(shiva,num))
# print(result)

# num=[1,2,3,4]
# sum=[5,6,7,8]
# k=list(map(lambda x,y:x+y,num,sum))
# print(k)


# num=[1,2,3,4,5,6]
# num2=[1,10,9,8]
# k=list(filter(lambda pair:(pair[0]+pair[1])%2==0,zip(num,num2)))
# print(k)

# ch=["shiva","nani","sai","Sdfghjkjhgfds"]
# print(list(filter(lambda x:len(x)>5,ch)))


# from functools import reduce
# num=["hii ","shiva ","how ","are ","you.."]
# k=list(map(lambda x:x+x,num))
# print(k)

# st=[{"name":"shiva","score":54},
#     {"name":"nani","score":14},
#     {"name":"mani","score":98},
#     {"name":"shire","score":76}]
# s=list(sorted(st,key=lambda x:x["score"]))
# print(s)

# l=[765,3456,7654,35432,23,43,34]
# s=(sorted(l,key=lambda x:x))
# print(s)

# n=list(map(int,input().split()))
# k=list(map(lambda x:(x*9/5)+32 ,n))
# print(k)

# l=["Shiva","mani","2nani"]
# k=list(filter(lambda x:x[0].isdigit(),l))
# print(k)

# l=[("shiva",22),("nani",32),("mani",13)]
# k=list(sorted(l,key=lambda x:x[1],reverse=True))
# print(k)


# def shiva(fun,lst):
#     result=[]
#     for i in lst:
#         result.append(fun(i))
#     return result
# def keka(x):
#     return x*2
# num=[1,2,3,4]
# k=shiva(keka,num)
# p=list(map(keka,num))
# print(k)
# print(p)
# from functools import reduce
# num=[1,2,3,4,5,6,7]
# # k=list(filter(lambda x:x%2==0,num))
# # p=list(map(lambda y:y*3,k))
# # l=list(sorted(p,key=lambda f:f))
# # g=reduce(lambda a,b:a+b,l)
# g=reduce(lambda a,b:a+b,list(sorted(map(lambda y:y*3,list(filter(lambda x:x%2==0,num))))))
# print(g)



# from functools import reduce
# numbers = [10, 25, 3, 18, 7, 40, 12, 5, 30]
# k=reduce(lambda a,b:a+b,sorted(list(filter(lambda r:r>200,list(map(lambda y:y**2,list(filter(lambda x:x>10,numbers))))))))
# print(k)

# from functools import reduce
# names = ["shiva", "nani", "sairam", "ravi", "mahesh", "anil", "suresh"]
# k=reduce(lambda x,y:x+" "+y,sorted(list(map(lambda x:x.upper(),list(filter(lambda x:len(x)>4,names))))))
# print(k)

# from functools import reduce
# students = [
#     ("Shiva", 78),
#     ("Nani", 92),
#     ("Sai", 65),
#     ("Ravi", 88),
#     ("Kiran", 55),
#     ("Arjun", 95)
# ]
# k=reduce(lambda a,b:a+b,sorted(map(lambda x:x[1]+5,list(filter(lambda x:x[1]>=70,students)))))
# print(k)

class a:
    def __init__(self,n):
        self.n=n
        self.ind=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.ind<=self.n:
            value=self.ind
            self.ind+=1
            return value
        else:
            raise StopIteration
k=a(10)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
# for i in k:
#     print(i)