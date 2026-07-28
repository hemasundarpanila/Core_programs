# '''def add(a, b):
#     print(a + b)
# x=add(10, 20)
# print(x)

# '''
# def fun():
#     return 50
# a=fun()
# print(a)

# '''def apply(a,b): 
#     return a(b)
 
# def double(x): 
#     return x*2 
 
# def square(x): 
#     print(x * x) 
 
# print(apply(double,10))
# apply(square,20)
# '''


def fun(fun3):
    def fun2():
        print("welcome to cvcorp")
        fun3()
        print("thankyou for visiting")
    return fun2
# @fun
fun3=fun(fun3)
def fun3():
    print("hello")
