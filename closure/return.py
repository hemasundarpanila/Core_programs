'''def fun2(a,b):
    print(a+b)
print(fun2(10,75))'''
n=5
p=2
c=0
while(True):
    fc=0
    for i in range(1,p+1):
        if(p%i==0):
            fc=fc+1
    if fc==2:
        print(i)
        c=c+1
        if c==n:
            break
    p=p+1
