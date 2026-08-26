# #largest of Element in an array
num = [55,41,86,97,22,1,99]
larg = num[0]
n = len(num)
for i in range (0,n):
    larg = max(larg,num[i])
print (larg)