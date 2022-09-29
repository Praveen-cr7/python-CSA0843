try:
    n=int(input("ENTER THE NUMBER OF ROWS---> "))
    if(n<=0):
        print("INVALID VALUE")
        exit()
    i=1
    while(i<=n):
        j=i
        while(j>=1):
            print(j,end=' ')
            j=j-1
        i=i+1
        print(" ")
except(ValueError):
    print("FLOAT VALUES")
    exit()
    
