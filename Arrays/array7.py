#find Largest sum contiguous Subarray
def max_subarray_with_indices(arr):
    current=arr[0]
    max=arr[0]
    start=0
    end=0
    temp=0
    for i in range(1,len(arr)):
        if arr[i]>current+arr[i]:
            current=arr[i]
            temp = i
        else:
            current +=arr[i]
        if current > max:
            max=current
            start=temp
            end=i
    return max, arr[start:end+1]
        
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_with_indices(arr))