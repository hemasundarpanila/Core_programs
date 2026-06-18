def f(x):
    k=(x**3)+53
    k=k+3*(x**2)
    return k
def g(y):
    m=(y**2)+1
    m=m+2*(y)
    return m
def v(x,y):
    return x*y
print(v(f(10),g(12)))
