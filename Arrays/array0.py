#0.Reverse the array without using the built in function
def reverse_array(arr):
    #left, right=0,len(arry)-1 (tuple operation)
    left=0
    right=len(arr)-1
    while left < right:
      arr[left],arr[right]=arr[right],arr[left]
      left+=1
      right-=1
    return arr
n=int(input("enter the number of elements in array: "))
arr=[]
for i in range(n):
    element=int(input("enter element:"))
    arr.append(element)
print("the original array is:",arr)    
print("the reverse of the array",reverse_array(arr)) #time O(n) , space O(1)
