def min_days(bloom_day: list[int], m: int, k: int) -> int:
    if m * k > len(bloom_day):
        return -1
    def can_make_bouquets(day):
        bouquets = 0
        flowers = 0
        for b in bloom_day:
            if b <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    low, high = min(bloom_day), max(bloom_day)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if can_make_bouquets(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
print(min_days([1,10,2,10,3,10],3,1))    