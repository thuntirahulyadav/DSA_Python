class Solution:
   def remove_duplicate(self,arr: list) -> list:
      if not arr: 
        return None
      seen=set()
      result=[]
      for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)  
      return result      
sol=Solution()
arr=[1,2,2,3,3,4,5]
print(sol.remove_duplicate(arr))