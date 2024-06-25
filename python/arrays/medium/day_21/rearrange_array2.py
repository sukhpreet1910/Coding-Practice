# If array do not have equal number of positive and negative elements 


def rearrange_array(nums):
    pos = []
    neg = []
    modified = [] * len(nums)
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    
    l_pos = len(pos)
    l_neg = len(neg)
    
    for i in range(len(nums)):
        if l_pos > 0:
            modified.append(pos[i])
            l_pos -= 1
        if l_neg > 0:
            modified.append(neg[i])
            l_neg -= 1

    return modified



nums = [1, 2, -4, -5, 3, 6]

modified = rearrange_array(nums)
print(modified)