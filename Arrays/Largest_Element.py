class Solution:
   def Largest(self,arr: list) ->int:
      if not arr:
         return None
      largest=arr[0]
      for num in arr:
         if num > largest:
            largest=num
      return largest          
sol=Solution()
arr=[1,2,3,4,5]
print(sol.Largest(arr)) 
arr1=[1,4,3,6,5]
print(sol.Largest(arr1)) 
