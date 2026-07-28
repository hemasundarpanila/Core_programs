




'''nums = [[1, 2], [3, 4], [5, 6]]
k=[]
result = list(map(lambda x:k.append(10), nums))
print("Result:", result)
print("Nums:", nums) '''




'''from functools import reduce
l=[1,2,3,4]
k=reduce(lambda x,y:x+y,l,10)
print(k)'''



'''num=[12,15,7,18,20,21,25]
k=list(filter(lambda x:(x%3==0 or x%5==0) and not (x%3==0 and x%5==0),num))
print(k)
'''

'''l=[1,2,3,4]
m=[10,20,30]
k=list(map(lambda x,y:x+y,l,m))
print(k)
'''


'''def dun(x):
    return x+6
p=dun(20)
print(p)'''
