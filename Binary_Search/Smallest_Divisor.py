import math
def smallest_div(nums,x):
    def get_sum(div):
        return sum(math.ceil(num/div)for num in nums)
    low,high = 1, max(nums)
    ans=high
    while low<=high:
        mid=(low+high)//2
        if get_sum(mid) <= x :
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
print(smallest_div([1,2,5,9],7))                    