
def mult(x):
    def inner(a):
        return a*x
    return inner
x=mult(3)
y=mult(5)
print(x(30))
print(y(25))
print(x.__name__)
print(y.__name__)



'''def outer():
    x=5
    def inner():
        y=8
        result=x+y
        print (result)
    return inner
a=outer()
#print(a())
a() '''