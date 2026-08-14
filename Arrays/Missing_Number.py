class solution:
    def missing_number(self,arr)->int:
        n = len(arr)
        total= (n*(n+1))//2
        return total - sum(arr)
sol=solution()
arr=[1,0,3]
print(sol.missing_number(arr))        