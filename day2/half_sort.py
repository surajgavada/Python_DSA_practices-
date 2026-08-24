#merge two sortest array
def merge_arr(left,right):
    result= []
    i,j=0,0
    n,m=len(left),len(right)
    while i <n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i < n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    print(result)

left = [1,2,3,4]
right = [1,2,3,4,5,6,7]
merge_arr(left,right)