class solution:
    def two_sum(self,arr,target)->list:
        seen = {}
        for i,num in enumerate(arr):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i 
        return []
sol=solution()
arr=[2,7,11,13]
target=9       
print(sol.two_sum(arr,target)) 