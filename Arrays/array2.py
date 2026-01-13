#2.Find the 'kth' max and min in the array
def kth_max_min(arr,k):
    arr.sort()
    if k > len(arr) or k<=0 :
        return print("invalid k value")
    kth_max = arr[len(arr)-k]
    kth_min = arr[k-1]
    return kth_max,kth_min
n=int(input("enter the number of elements in array:"))
arr=[]
for i in range (n):
    element=int(input("enter element:"))
    arr.append(element)
k=int(input("enter the value of k:"))
kth_max,kth_min=kth_max_min(arr,k)
print(f"{k} th maximum element is: {kth_max}")
print(f"{k} th minimum element is: {kth_min}") #time O(n log n), space O(1)
