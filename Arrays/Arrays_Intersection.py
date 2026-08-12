class solution:
    def intersection(self, arr1 :list, arr2 :list)->list:
             set1=set(arr1)
             set2=set(arr2)

             return list(set1.intersection(set2))   

sol=solution()
arr1=[0,1,7,5] 
arr2=[2,4,5,9]
print(sol.intersection(arr1,arr2))
 