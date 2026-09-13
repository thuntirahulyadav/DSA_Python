import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def calculate_total_hours(speed):
        return sum(math.ceil(p / speed) for p in piles)

    low, high = 1, max(piles)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if calculate_total_hours(mid) <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
print(min_eating_speed([3,6,7,11],8))