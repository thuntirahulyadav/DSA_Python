class Solution:
   def Second_largest(self,arr: list) ->int:
     if not arr:
        return None
     largest=float('-inf')
     sec_largest=float('-inf')
     for num in arr:
        if num > largest:
            sec_largest=largest
            largest=num
        elif num > sec_largest and num!=largest:
            sec_largest=num

     return sec_largest if sec_largest!=float('-inf') else -1         
sol=Solution()
arr=[1,2,3,4,5]
print(sol.Second_largest(arr))  