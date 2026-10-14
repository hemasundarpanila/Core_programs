with open("transaction.txt","r")as t,\
    open("clean.txt","w")as c,\
    open("error.txt","w")as err:
    t.readline()

    total_lines=0
    clean_lines=0
    error_lines=0
    total_amount=0
    cat_amount={}

    for line in t:
        total_lines+=1
        u,a,cat=line.split(",")

        try:
            if cat==" " or a==" " or u==" ":
                raise ValueError("cannot have empty or null")
            a=int(a)
            if a<0:
                raise ValueError("amount can not be negative")
            c.write(f"{line}")
            clean_lines+=1
            total_amount+=a
            cat_amount[cat]=cat_amount.get(cat,0)+a
        except ValueError as e:
            error_lines+=1
            err.write(f"{line}->{e}\n")
            err.flush()
with open("report.txt","w")as r:
    r.write(f"{total_lines}lines processed\n")
    r.write(f"{clean_lines}lines cleaned\n")
    r.write(f"{error_lines}lines error\n")
    r.write(f"{total_amount}lines processed\n")

    for cat,amount in cat_amount.items():
        r.write(f"{cat} -> {amount}\n")


# l=[1,2,3,1,2]
# d={}
# for i in l:
#     d[i]=d.get(i,0)+1
# print(d)
