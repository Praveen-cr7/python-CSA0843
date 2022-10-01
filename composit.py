sr=int(input("a"))
if(sr<=0):
    print("invalid")
    exit()
er=int(input("b"))
if(er<=0):
    print("invalid")
    exit()
if(sr==er):
    print("both cant be the same value")
    exit()
elif(sr>er):
    print("large value")
    exit()
else:
    f=0
    for i in range(sr+1,er):
        f=0
        for j in range(1,j):
            if(i%j==0):
                f+=1
        if(f>1):
            print(i)
