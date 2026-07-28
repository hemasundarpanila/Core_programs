from functools import reduce
def cal(*a,op):
    def add():
        return reduce(lambda x,y:x+y,*a)
    def sub():
        return reduce(lambda x,y:x-y,*a)
    if op=="+":
        return add()
    if op=="-":
        return sub()
c=input("operation:")
print(cal((1,2,3,4),op=c))
    
    




'''def cal(fun,*v1):
    return fun(*v1)
def add():
    return x+y
def sub():
    return x-y
def mul():
    return x*y
print(cal(add,10,20,30,40))'''""