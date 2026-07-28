def double(x):
    return x*2
def triple(x):
    return x*3
def quadruple(x):
    return x*4
def apply_all(funcs,value):
    for i in funcs:
        value=i(value)
    return value
funcs=[double,triple,quadruple]
print(apply_all(funcs,5))





'''def make(name,prefix="hello",formater=(lambda x:x)):
    greeting= prefix +""+ name
    return formater(greeting)
greeting=make("shiva")
print(make("shiva",formater=str.upper))'''



'''def make_greeting(name, prefix="Hello", formatter=lambda x: x):
    greeting = prefix + " " + name
    return formatter(greeting)

print(make_greeting("Shiva"))

print(make_greeting("Shiva", formatter=str.upper))
'''
'''def apply(a,b,op):
    return op(a,b)
print(apply(10,5,lambda x,y:x+y))
print(apply(10,5,lambda x,y:x-y))
print(apply(10,5,lambda x,y:x*y))
'''