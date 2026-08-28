class solution:
    def left_rotate_one(self, arr : list)->list:
        if not arr:
            return arr
        temp=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[-1]=temp
        return arr
sol=solution()
arr=[1,2,3,4,5]  
print(sol.left_rotate_one(arr)) 