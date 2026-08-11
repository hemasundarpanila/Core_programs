class Number:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return Number(self.value - other.value)
    def __add__(self,w1):
        return Number(self.value+w1.value)
    def __mul__(self,w2):
        return Number(self.value*w2.value)
    def __mod__(self,w3):
        return Number(self.value%w3.value)
    def __str__(self):
        return f"{self.value}"

a = Number(10)
b = Number(20)
d=Number(40)
f=Number(20)

print((a - b - d-f))
print((a +b + d+f))
print((a *b * d*f))
print((a % b % d%f))


# class values:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self,other):
#         return values(self.value+other.value)
#     def __str__(self):
#         return f"{self.value}"
# a=values(10)
# b=values(20)
# c=values(30)
# e=a+b+c
# print(e)

# l=list(map(int,input().split()))
# h1=float("-inf")
# h2=h1
# for i in range(len(l)):
#     if (l[i]>h1):
#         h2=h1h1=l[i]
#     elif ()