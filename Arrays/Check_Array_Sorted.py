class Solution:
   def check_sorted(self,arr: list) ->bool:
     if not arr:
        return None
     for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
     return True          
              
sol=Solution()
arr1=[1,2,4,3,5]
print(sol.check_sorted(arr1))
arr2=[1,2,3,4,5]
print(sol.check_sorted(arr2))
