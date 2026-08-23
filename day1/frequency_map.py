n = [1,2,4,6,2,1,4,8,8,5,1,3,3]
dict = {}
for i in range (0 ,len(n)):
    if n[i] in dict:
        dict[n[i]]+=1
    else:
        dict[n[i]]=1
print(dict)
