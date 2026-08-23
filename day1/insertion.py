def insertion_s(n):
    key = 0
    for i in range(1,len(n)):
        key = n[i]
        j =i-1
        while j >= 0 and n[j] > key:
            n[j+1] = n[j]
            j -=1
        n[j+1] =key
n = []
arr = int(input("Enter no of element:"))
for i in range (arr):
    num = int(input(f"{i+1}:"))
    i += 1
    n.append(num)
insertion_s(n)
print(n)