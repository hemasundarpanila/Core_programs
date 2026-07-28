x=5
def fun():
    def inner():
        print(x)
    return inner
a=fun()#inner
a()