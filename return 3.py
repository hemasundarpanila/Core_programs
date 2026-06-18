def fun(a,b):
    return a*b
def fun2(x,y):
    return x+y
k=fun(7,8)
m=fun(10,20)
print(fun(k,m))
print(fun2(fun(7,8),fun(10,20)))
