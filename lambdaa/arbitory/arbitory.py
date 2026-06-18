def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print(fun(name="shiva",age="23",hobby="music"))
 




'''def fun(*a):
    t=0
    for i in a:
        t=t+i
    return t
print(fun(1,2,3,4,5))'''





'''def fun(*a):
    print(a)
    print(*a)
fun(1,2,3,4)'''
