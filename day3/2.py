 #largest of Element in an array
num = [55,41,86,97,22,1,99]
larg = num[0] #here we just take first index
n = len(num)
for i in range (0,n):
    larg = max(larg,num[i])
print (larg)

# #largest of Element in an array
num = [55,41,86,97,22,1,99]
larg = float("-inf") #here we use -infinite
n = len(num)
for i in range (0,n):
    larg = max(larg,num[i])
print (larg)