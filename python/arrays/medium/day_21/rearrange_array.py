def brute_rearrange_array(nums):
    pos = []
    neg = []
    modified = []
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    
    for i in range(len(pos)):
        modified.append(pos[i])
        modified.append(neg[i])

    return modified



def rearrange_array(nums):
    
    pos = 0
    neg = 1
    modified = [0] * len(nums)
    for i in range(len(nums)):
        if nums[i] < 0:
            modified[neg] = nums[i]
            neg += 2
        else:
            modified[pos] = nums[i]
            pos += 2
    return modified






nums = [3,1,-2,-5,2,-4]

modified = rearrange_array(nums)
print(modified)