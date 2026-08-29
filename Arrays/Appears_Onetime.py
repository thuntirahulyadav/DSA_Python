class solution:
    def Number_appears_ones(self,arr)->int:
         xor=0
         for num in arr:
            xor^=num
         return xor   
sol=solution()
arr=[5,3,4,2,5]
print(sol.Number_appears_ones(arr)) 
