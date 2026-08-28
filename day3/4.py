arr = []
n = int(input("enter lenght of array:"))
for i in range (n):
    num = int(input(f"the element is {i+1} :"))
    arr.append(num)

m = len(arr)
for i in range (0,m-1):
    if arr [i] > arr[i+1]:
        print("arr is not sorted")
        break
else:
    print("arr is sorted")