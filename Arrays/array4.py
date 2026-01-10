#Move all the negative elements to one side of the array
def move_negative(arr):
    j=0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    return arr
n=int(input("enter the number of elements in array:"))
arr=[]
for i in range(n):
    element=int(input("enter element:"))
    arr.append(element)
print("the original array is:",arr)    
print("the array after sort",move_negative(arr))      