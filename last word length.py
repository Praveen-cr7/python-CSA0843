def length(str):
    li=list(str.split(" "))
    return len(li[-1])
str=input("enter a string:")
print("length of last word:",length(str))
