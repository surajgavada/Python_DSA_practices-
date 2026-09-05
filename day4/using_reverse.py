def reverse(num,right,left):
    while right<left:
        num[right],num[left] =num[left],num[right] 
        right += 1
        left -=1

num =[6,4,8,2,3,4,7]
n=len(num)
k=3
reverse(num,n-k,n-1)
reverse(num,0,n-k-1)
reverse(num,0,n-1)
print(num)