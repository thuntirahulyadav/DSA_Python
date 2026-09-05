def get_floor_ceil(arr, target):
    low,high=0,len(arr)-1
    floor,ceil=-1,-1
    while low <= high :
        mid=(low+high)//2
        if arr[mid]==target:
            return (arr[mid],arr[mid])
        elif arr[mid]<target:
            floor = arr[mid]
            low = mid+1
        else:
            ceil = arr[mid]
            high = mid-1
    return (floor,ceil)            
print(get_floor_ceil([1,2,3,4,6,7],5))