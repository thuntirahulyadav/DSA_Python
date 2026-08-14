class solution:
    def subarray_count(self,arr,k)->int:
         prefix_map={0:1}
         curr_sum=0
         count=0
         for num in arr:
            curr_sum += num
            needed_sum = curr_sum - k
            if needed_sum in prefix_map:
                count += prefix_map[needed_sum]
            prefix_map[curr_sum]=prefix_map.get(curr_sum,0) + 1   
         return count     
sol=solution()
arr=[1,2,1,3]
k=3
print(sol.subarray_count(arr,k))  