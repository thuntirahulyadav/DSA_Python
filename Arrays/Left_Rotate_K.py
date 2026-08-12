class solution:
    def left_rotate_k(self, arr : list,k : int)->list:
        n=len(arr)
        if n == 0 :
            return arr
        k = k % n
        def reverse(sub,start,end):
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        reverse(arr,0,k-1)
        reverse(arr,k,n-1)
        reverse(arr,0,n-1)
        return arr        
sol=solution()
arr=[1,2,3,4,5] 
k=3
print(sol.left_rotate_k(arr,k)) 