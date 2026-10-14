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

# with open("shiva.txt","r")as s:
#     print(s.read())
#     print(s.tell())
# l=["hi","how","are","you"]
# with open("shiva.txt","w+")as s:
#     s.writelines(l)
#     print(s.read())

# f=open("test.txt","r")
# print(f.read())# full file text
# f.seek(0)#f.tell()
# print(f.readline())#
# f.seek(0)
# print(f.readlines())
# f.seek(0)
# file=open("test1.txt","x")
# file.truncate(10)

# with open('test.txt', 'w+') as f,open('test.txt', 'a') as g:
#     f.write('Hello World')
#     f.seek(0)
#     print(f.read())
#     f.write("test")
#     f.close()
#     g.write('Hello World\n')
#     g.write("test")

#class


# class A:
#     def __init__(self,fn):
#         self.fn = fn
#     def __enter__(self):
#         print("entering file")
#         self.f=open(self.fn,'r')
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Closing file")
#         self.f.close()
# obj=A("test.txt")
# with obj as f:
#     f.seek(0)
#     print(f.read())



# import contextlib

# @contextlib.contextmanager
# def f(fn):
#     print("entering file")
#     x=open(fn,'r')
#     try:
#         yield x
#     finally:
#         print("closing file")
#         x.close()

# with f("test.txt") as f:
#     print(f.read())