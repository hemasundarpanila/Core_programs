def fun4(*a,**b):
    print(a,b,sep="\n")
    print(type(a),type(b))
fun4(1,23,23,234,34,45,c=30,f=45)
