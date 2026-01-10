#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
def rahul(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid <= high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
n=int(input("enter the number of elements in array:"))
arr=[]
for i in range(n):
    element=int(input("enter element:"))
    arr.append(element)
print("the original array is:",arr)    
print("the array after sort",rahul(arr)) 