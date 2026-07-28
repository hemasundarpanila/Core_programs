'''a=100
def fun():
    x=300
    def fun2():
        nonlocal x
        x=200
        print(x)
    print(x)
    fun2()
    print(x)
fun()'''



'''a=50
def fun():
    x=200
    def fun2():
        y=300
        print(y,x,a)
    fun2()
fun()
'''


x=10
def fun():
    global x
    x=300
print(x)
fun()
print(x)
