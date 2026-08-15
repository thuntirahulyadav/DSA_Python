class solution:
    def max_subarray_sum(self,arr)->int:
        maximum = float('-inf')
        curr_sum = 0
        for num in arr:
            curr_sum += num
            maximum = max(maximum , curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return maximum          

sol=solution()
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(sol.max_subarray_sum(arr)) 