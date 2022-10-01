try:
    sal=float(input("enter the salay"))
    if(sal<=0):
        print("byeee")
        exit()
    ch=input("enter the grade")
    print("salary",sal)
    if(ch=='A' or ch=='a'):
        bon=sal*5/100
        tot=bon+sal
        print("bonus",bon)
        print("total salary",tot)
    elif(ch=='B' or ch=='b'):
            bon=sal*10/100
            tot=bon+sal
            print("bonus",bon)
            print("total salary",tot)
    else:
            print("invalid")
            exit()
    if(sal<10000):
     if(ch=='A' or ch=='a'):
                bon=sal*7/100
                tot=ban+sal
                print("bonus",bon)
                print("total salary",tot)
    elif(ch=='B' or ch=='b'):
                bon=sal*12/100
                tot=ban+sal
                print("bonus",bon)
                print("total salary",tot)
    else:
                print("invalid entry")
                exit()
except(valueError):
        print("error")
        exit()
