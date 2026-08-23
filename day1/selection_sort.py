def selection_sort(num):
    n = len(num)
    for i in range (n-1):
        min_ind = i
        for j in range (i+1,n):
            if num[j] < num [min_ind]:
                min_ind = j
        num[i],num[min_ind] = num[min_ind], num[i]
    return

n = int( input("Enter the number of elements:"))
num =[]
for i in range(n):
    arr = int(input(f"Element {i+1}:"))
    num.append(arr)
print("Before sort in the element:",num)
selection_sort(num)
print("after sorting the elements:",num)