num = [88,4,66,95,74,85,89,1]
largest = float("-inf")
s_largest = float("-inf")
n = len(num)
for i in range (n):
    largest = max(largest,num[i])
for i in range (n):
    if num[i] > s_largest and num[i] != largest:
        s_largest = num[i]
print(s_largest)
