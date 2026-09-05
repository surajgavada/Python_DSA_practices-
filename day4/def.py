def rotation(num, k=3):
    n = len(num)
    # if n == 0:
    #     return num

    r = k % n
    for _ in range(r):
        e = num.pop()
        num.insert(0, e)
    # return num


num = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    arr = int(input(f"Element {i+1}: "))
    num.append(arr)

rotation(num)
# print("Rotated list:", num)