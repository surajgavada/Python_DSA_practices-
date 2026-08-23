def pal(n):
    left = 0
    right= len(n)-1
    while left <right:
        if n[left]!= n[right]:
            return "it is not a palidrome"
        left +=1
        right -=1
    return "it is a palindrome "
print(pal(input("Enter your number: ")))