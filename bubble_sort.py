def bubble(nums):
    n = len(nums)
    for i in range (n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]

n = int (input("Enter the number of elements: "))
nums =[]
for i in range(n):
    arr = int(input(f"the element is {i+1}:"))
    nums.append(arr)

print(nums)
bubble(nums)
print(nums)
