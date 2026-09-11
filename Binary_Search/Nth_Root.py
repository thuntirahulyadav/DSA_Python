def nth_root(n,m):
    def check(mid,n,m):
        ans=1
        for _ in range(n):
            ans*=mid
            if ans > m:
                return 2
        if ans==m:
            return 1
        return 0
    low,high=1,m
    while low<=high:
        mid=(low+high)//2
        status=check(mid,n,m)
        if status == 1:
            return mid
        elif status == 0:
            low=mid+1
        else:
            high=mid-1
    return -1    
print(nth_root(3,27))     