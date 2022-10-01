a=[(1,3)]
print("the original list is:"+str(a))
res=[(sub[1],sub[0]) for sub in a]
print("the swap tuple list:"+str(res))
