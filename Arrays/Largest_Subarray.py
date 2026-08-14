class solution:
    def largest_subarray(self,arr,k)->int:
         prefix_map={0:-1}
         curr_sum=0
         maximum=0
         for i,num in enumerate(arr):
            curr_sum += num
            needed_sum = curr_sum - k
            if needed_sum in prefix_map:
               maximum = max(maximum, i- prefix_map[needed_sum]) 
            if curr_sum not in prefix_map:
               prefix_map[curr_sum]=i 
         return maximum     
sol=solution()
arr=[1,2,1,3]
k=3
print(sol.largest_subarray(arr,k))  