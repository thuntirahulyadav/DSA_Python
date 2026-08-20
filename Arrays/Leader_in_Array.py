def leaders_of_array(arr)->list:
    leaders =[]
    max_right= float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    leaders.reverse()
    return leaders        
arr = [10,22,12,3,0,6]    
print(leaders_of_array(arr)) 