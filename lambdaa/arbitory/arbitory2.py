def fun3(a,b,c):
    print(a,b,c)
def fun2(**d):
    print(d)
    fun3(**d)
fun2(a=1,b=2,c=3)
fun3(a=10,b=20,c=30)
