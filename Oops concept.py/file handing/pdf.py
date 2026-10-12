'''• Write a Python program using a context manager (with) to open a text file in 
read mode, read the entire content using read(), and print the number of 
characters in the file.
'''
# with open("shiva.txt","r")as s:
#     data=s.read()
#     print("number of characters:",len(data))

'''• Write a program that opens a file using a context manager, reads all lines 
using readlines(), and prints only the lines that contain more than 10 
characters.'''

# l=["hello\n","shiva\n","hii\n"]
# with open("shiva.txt","w")as s:
#     s.writelines(l)

# with open("shiva.txt","r")as s:
#     data=s.readlines()
#     for i in data:
#         if len(i.strip())>3:
#             print(i)

'''• Write a program that creates a file and writes 3 lines using write(), reopens 
the same file in append mode, appends 2 more lines, and finally reads and prints 
the complete file content.
'''

# l=["happy new year\n","happy dasara\n","happy diwali"]

# with open("shiva.txt","w")as s:
#     s.write("happy new year\n")
#     s.write("happy dasara\n")
#     s.write("happy diwali\n")
# with open("shiva.txt","r")as s:
#     print(s.read())
# with open("shiva.txt","a")as s:
#     s.write("happy ugadhi\n")
#     s.write("happy pongal\n")
# with open("shiva.txt","r")as s:
#     print(s.read())


'''• Write a program that opens a file in read mode, reads the first 10 characters, 
prints the current cursor position using tell(), moves the cursor back to the 
beginning using seek(0), and reads the full content again.'''

# with open("shiva.txt","r")as s:
#     data=s.read(10)
#     print("10 characters:",data)
#     print("present position:",s.tell())
#     s.seek(0)
#     print("complete content:",s.read())

