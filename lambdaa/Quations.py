l=[1,2,3,4,5,6,7,8,9]
k=list(filter(lambda x:x%3==0,l))
s=list(map(lambda x:x**2,k))
print(s)


'''def fun(name,prefix="Hello",formatter=lambda x:x):
    m=f"{name} {prefix}"
    return formatter(m)
print(fun("ramu",formatter=str.upper))
'''


'''def fun(a,b,ok):
    return ok(a,b)
print(fun(10,20,lambda x,y:x+y)) '''