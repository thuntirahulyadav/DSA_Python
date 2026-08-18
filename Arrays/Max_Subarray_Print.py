class solution:
    def max_subarray(self,arr)->list:
        maximum = float('-inf')
        curr_sum=0
        start=0
        ans_start=0
        ans_end=0
        for i,num in enumerate(arr):
            curr_sum+=num
            if curr_sum > maximum:
                maximum = curr_sum
                ans_start = start
                ans_end = i
            if curr_sum < 0:
                curr_sum=0
                start = i+1    
        return arr[ans_start:ans_end+1]     

sol=solution()
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(sol.max_subarray(arr))