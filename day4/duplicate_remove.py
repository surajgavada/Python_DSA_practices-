num = [1,1,1,2,3,3,4,4,5,6,6,7,7,7,]
n = len(num)
freq_map = {}
for i in range(0,n-1):
    freq_map[num[i]]=0
j = 0
for k in freq_map:
    num[j] = k
    j += 1
print("Unique values:", num[:j])

# num = [1,1,1,2,3,3,4,4,5,6,6,7,7,7,]
# result = []
# for i in num:
#     if i not in result:
#         result.append(i)
# print("after removing the duplicate arrays:",result)