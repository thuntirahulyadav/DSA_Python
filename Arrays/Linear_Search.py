class solution:
    def linear_search(self, arr :list, target :int)->int:
       if not arr:
         return -1
    
       for i in range(len(arr)):
            if arr[i]==target:
                return i      
       return -1 

sol=solution()
arr=[0,1,7,3,4] 
target=4
result=sol.linear_search(arr,target)
if result != -1 :
   print(f"the element {target} found in index {result}")
else:
    print(f"the element {target} not found")    