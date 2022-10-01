1 BREAD LOAVES
2 ISOSTRING
3 WATER TANK
4 STAIR CASE
5 TRADING
6 VOWEL
7 BINARY ADDITION
mylist = []
n =int(input("enter length of list:"))
for a in range(1,n+1):
    e = int(input("enter element:"))
    mylist.append(e)
print(mylist)
l = len(mylist)
prime = []
composite = []
for i in range(0,n):
    c=0
    for j in range(2,mylist[i]):
        if mylist[i]%j == 0:
            c =1
            break
    if c==0:
        prime.append(mylist[i])
    else:
        composite.append(mylist[i])
print("prime number list")
print(prime)
prime_count=len(prime)
print("length of prime",prime_count)
print("composite number list")
print(composite)
composite_count=len(composite)
print("length of composite",composite_count)
