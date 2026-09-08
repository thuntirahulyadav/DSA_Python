def find_rotation_count(arr):
    low,high = 0,len(arr)-1
    min_val=float('inf')
    min_index=-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            if arr[low]< min_val:
                min_index=low
            break
        if arr[low]<=arr[mid]:
            if arr[low]< min_val:
                min_val=arr[row]
                min_index=row
            low=mid+1
        else:
            if arr[mid]< min_val:
                min_val=arr[mid]
                min_index=mid
            high=mid-1
    return min_index
arr=[6,7,1,2,3,4,5]
print(find_rotation_count(arr))      