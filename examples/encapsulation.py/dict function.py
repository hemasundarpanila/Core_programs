def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
op={
    "+":sum,
    "-":sub,
    "*":mul
}
op1="+"
print(op[op1](10,20))