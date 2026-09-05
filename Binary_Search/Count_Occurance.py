def get_first_last(arr,target) :
  def get_first():
    low,high=0,len(arr)-1
    first=-1
    while low <= high :
        mid=(low+high)//2
        if arr[mid]==target:
           first=mid
           high = mid-1
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return first 
  def get_last():
    low,high=0,len(arr)-1
    first=-1
    while low <= high :
        mid=(low+high)//2
        if arr[mid]==target:
           last=mid
           low = mid+1
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return last
  return [get_first(),get_last()]  
def count_occurance(arr,target):
    first,last = get_first_last(arr,target)
    if first == -1:
        return 0
    return last-first+1      
print(count_occurance([1,2,3,4,4,4,4,6,7],4))