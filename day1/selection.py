def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [5,2,4,8,9,6,1]

print("Original array:", arr)

selection_sort(arr)

print("Sorted array:", arr)