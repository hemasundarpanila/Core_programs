"""def fun(x):
    if x not in "AEIOUaeiou":
        return x
    return ""
l=["shiva","mangolo","mani"]
k=[]
for i in l:
    m=list(map(fun,i))
    m="".join(m)
    k.append(m)
print(k)"""




'''def fun2(a,b):
    print("list1:",sum(a))
    print("list2",sum(b))
    print("total:",sum(a+b))
fun2([1,2,3,4,5],[6,7,8,9,10])'''
"""d={"apple":100,"banana":40,"cherry":150}
m=list(filter(lambda x:x[1]>50,d.items()))
print(m)"""

from functools import reduce
num=[5,10,15,20,25,30]
k=reduce(lambda x,y:x+y,list(filter(lambda x:x%5==0,list(map(lambda x:x**2,num)))))
print(k)


    
