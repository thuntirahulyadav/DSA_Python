def find_min(arr):
    low,high=0,len(arr)-1
    ans=float('inf')
    while low <= high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            ans=min(ans,arr[low])
            break
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1     
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans
print( find_min([6,7,8,1,2,3,4,5]) )   