def sumofsquare(n):
    en=0
    on=0
    for i in range(0,n):
        if(arr[i]%2==0):
            en=en+(arr[i]*arr[i])
        else:
            on=on+(arr[i]*arr[i])
    return(en,on)
n=int(input("ELEMENTS NO---> "))
arr=[]
for i in range(0,n):
    a=int(input("Element---> "))
    arr.append(a)
print(sumofsquare(n))
