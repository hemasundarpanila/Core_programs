profile={"username":"","name":"","phno":"","email:":""}
def register():
    k={}
    global profile
    k["name"]=input("enter your name:")
    k["phno"]=input("enter your phno:")
    k["email"]=input("enter your email:")
    while(True):
        un=input("enter your username:")
        if un in profile.keys():
            print("user name alresy exist")
            continue
        profile[un]=k
        break