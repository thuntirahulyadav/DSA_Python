#1.Find the maximum and minimum element in an array
def find_max_min(arr):
    maximum = minimum = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]
        elif arr[i]<minimum:
            minimum=arr[i]
    return maximum,minimum
n=int(input("enter the number of elements in array:")) 
arr=[]
for i in range(n):
    element=int(input('enter element:')) 
    arr.append(element)
max_val,min_val=find_max_min(arr)
print("the max value is:",max_val)
print("the min value is:",min_val)  #time O(n), space O(1)            