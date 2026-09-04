def upper_bound(arr,target):
    low , high = 0 , len(arr)-1
    ans = len(arr)
    while low <= high:
        mid=(low+high)//2
        if arr[mid]>target:
            ans = mid 
            high = mid - 1
        else :
            low = mid + 1 
    return ans   

print("The Upper Bound of the element is:", upper_bound([1,2,3,4,5,5,7],5) )  