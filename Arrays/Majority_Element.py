class solution:
    def majority_element(self,arr)->int:
        count=0
        cadidate=None
        for num in arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate        
        
        
sol=solution()
arr=[2,2,1,1,1,2,2]
print(sol.majority_element(arr)) 