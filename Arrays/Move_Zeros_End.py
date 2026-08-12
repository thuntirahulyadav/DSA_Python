class solution:
    def Move_zeros_end(self, arr : list)->list:
       if not arr:
         return arr
       position = 0
       for i in range(len(arr)):
            if arr[i]!=0:
                arr[position],arr[i]=arr[i],arr[position]
                position+=1
       return arr 
               
sol=solution()
arr=[0,1,0,3,12] 
print(sol.Move_zeros_end(arr)) 