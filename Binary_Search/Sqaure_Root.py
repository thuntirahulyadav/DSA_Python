def square_root(num):
    if n==0 or n==1:
        return num
    low,high=1,num
    ans=1
    while low<=high:
        mid=(low+high)//2
        if mid*mid <= n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
n=30
print(square_root(n))       