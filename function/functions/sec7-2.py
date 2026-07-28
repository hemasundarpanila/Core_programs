def fun(x):
    return x.capitalize()
def fun2(x):
    return x.lower()
def fun3(x):
    return x.title()
operations={
    "upper":fun,
    "lower":fun2,"title":fun3
}
op="lower"
print(operations[op]("SHIVA"))

  







'''def fun(fun1,value):
    return fun1(value)
def fun2(x):
    return x*2
def fun3(x):
    return x*x
print(fun(fun2,5))
print(fun(fun3,5))'''
