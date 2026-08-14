class solution:
    def max_consecutive_ones(self,arr)->int:
        if not arr: 
            return arr
        count = 0
        maximum = 0    
        for i in range(len(arr)):
            if arr[i] == 1:
               count += 1
               maximum = max(maximum,count)
            else:
                count = 0   
        return maximum       
sol=solution()
arr=[1,1,0,1,1,1]
print(sol.max_consecutive_ones(arr))