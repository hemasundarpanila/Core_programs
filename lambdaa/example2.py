def fun(x):
    if x not in "AEIOUaeiou":
        return x
    return ""
l=[["shiva","rohith"],["mangala","nani"]]
k=[]
for i in l:
    s=list(map(lambda x:list(map(lambda y: "".join(map(fun,y)),x)),l))
    k.append(s)
print(k)





'''a=[["shiva","rohith"],["mangala","nani"]]
b="AEIOUaeiou"
k=list(filter(lambda x:list(filter(lambda y:y not in b ,x),a)))
print(k)
'''




'''from functools import reduce
l=[5,10,15,20,25,30]
k=list(map(lambda x:x**2,l))
h=list(filter(lambda y:y%5==0,k))
g=reduce(lambda a,b:a+b,h)
print(k)
print(h)
print(g)'''

'''k=list(map(str, [1, 2, 3]))
print(k)
m=list(map(lambda x: str(x), [1, 2, 3])) 
print(m)'''
 

'''l=[10,350,10,350,20]
k=list(map(lambda x:id(x),l))
print(k)'''


'''from functools import reduce
s=['P', 'y', 't', 'h', 'o', 'n']
k=reduce(lambda x,y:x+y,s)
print(k)'''

'''l=[["shiva"],["nani"]]
k=list(map(lambda x:list(filter(lambda y: y not in "AEIOUaeiou",x)),l))
print(k)
'''



'''from functools import reduce
l=[1,4,3,2,5,7]
k=reduce(lambda x,y:x if x>y else y,l)
print(k)
'''



'''d = {"apple": 100, "banana": 40, "cherry": 150} 
k=list(filter(lambda x:x[1]>50,d.items()))
print(k)'''


'''l=[[1,2],[3,4],[5,6]]
k=list(map(lambda x:list(map(lambda y:y+5,x)),l))
print(k)'''



'''def fun(a,b,*arg,position="defalt",**kws):
    print(a,b,arg,position,kws)
fun(1,2,3,4,5,position="changed",name="Alice",age=21)'''