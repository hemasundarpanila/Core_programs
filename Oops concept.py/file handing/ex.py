# f=open("data.txt","w")
# f.write("hello shiva")
# f.close()

# f=open("data.txt","r")
# data=f.read()
# print(data)
# f.close()

# f = open("data.txt", "r")
# print(f.read())
# f.close()

# with open("data.txt","w")as f:
#     f.write("hello shiva3")
# with open("data.txt","r")as f:
#     data=f.read()
#     print(data)
# f=open("data.txt","r")
# data=f.read()
# print(data)
# f.close()




# with open("data.txt","w")as p:
#     p.write("happy new year")
# with open("data.txt","r")as p:
#     data=p.read()
#     print(data)
# with open("data.txt","a")as p:
#     p.write("happy birthday")
# with open("data.txt","r")as p:
#     data=p.read()
#     print(data)
# with open("data.txt","r+")as p:
#     print(p.read())
#     p.write("welcome")

# with open("data.txt","r")as p:
#     data=p.read()
#     print(data)

# with open("data.txt","w+")as s:
#     s.write("mass")
#     # s.seek(0)
#     print(s.read())

# with open("data.txt","w")as s:
#     s.write("shiva")
# with open("data.txt","r")as s:
#     print(s.read())


# with open("shiva.txt","w")as s:
#     s.write("PANILA")
# with open("shiva.txt","r")as s:
#     print(s.read())

# with open("shiva.txt","w")as s:
#     s.write("jataraaa")
# with open("shiva.txt","r")as s:
#     print(s.read())
# with open("shiva.txt","w")as s:
#     s.write("happy new ywar")
# with open("shiva.txt","r")as s:
#     print(s.read())

# with open("shiva.txt","r+")as s:
#     s.write("welcome a")
# # with open("shiva.txt","r+")as s:
#     print(s.read())

# with open("shiva.txt","w+")as s:
#     s.write("check check")
#     s.seek(0)
#     print(s.read())

with open("shiva.txt","r")as s:
    print(s.read())
    print(s.tell())
l=["hi","how","are","you"]
with open("shiva.txt","w+")as s:
    s.writelines(l)
    print(s.read())