def rearrange_elements(arr)->list:
    n = len(arr)
    result = [0]*n
    pos_index=0
    neg_index=1
    for num in arr:
        if num > 0:
            result[pos_index]=num
            pos_index+=2
        else:
            result[neg_index]=num
            neg_index+=2   
    return result
arr = [3,1,-2,-1,2,-3]    
print(rearrange_elements(arr))
