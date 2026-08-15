class solution:
    def union(self, arr1 :list, arr2 :list)->list:
        seen=set()
        result=[]
        for num in arr1:
            if num not in seen:
                seen.add(num)
                result.append(num)
        for num in arr2:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result                

sol=solution()
arr1=[0,1,7,5] 
arr2=[2,4,5,9]
print(sol.union(arr1,arr2))