nums = [4, 1, 7, 6, 3, 2, 8]

def partition(nums, low, high):
    pivot = nums[low]

    i = low
    j = high

    while i < j:

        while nums[i] <= pivot and i < high:
            i += 1

        while nums[j] > pivot and j > low:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]

    return j


def Quick_sort(nums, low, high):

    if low < high:
        p_ind = partition(nums, low, high)

        Quick_sort(nums, low, p_ind - 1)
        Quick_sort(nums, p_ind + 1, high)


Quick_sort(nums, 0, len(nums) - 1)

print(nums)