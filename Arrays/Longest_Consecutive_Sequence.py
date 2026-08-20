def longest_consecutive(arr):
    num_set = set(arr)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr_num=num
            curr_streak=1 
            while curr_num+1 in num_set:
                curr_num+=1
                curr_streak+=1
            longest = max(longest,curr_streak) 
    return longest
arr=[100,1,200,2,3,4]
print(longest_consecutive(arr))               