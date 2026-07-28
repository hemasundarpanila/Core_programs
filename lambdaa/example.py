'''l="shIva"
k=list(filter(lambda x:x not in "AEIOUaeiou",l))
print(k)'''



'''l=[12,15,7,18,20,21,25]
k=list(filter(lambda x:(x%3==0 or x%5==0) and not(x%3==0 and x%5==0),l))
print(k)'''

l="mangala"
k=list(filter(lambda y:y not in  "AEIOUaeiou",l))
s= "".join(k)
print(s)


'''l="shiva panila"
k=list(map(lambda x:ord(x),l))
print(k)'''