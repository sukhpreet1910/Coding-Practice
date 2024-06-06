# Brute Using two pointer approach
# while j < length
#      [1, 1, 0, 0, 0, 0, 2, 4, 0, 5]
#      [1, 0, 0, 0, 0, 0, 2, 4, 0, 5]
#      [1, 2, 0, 0, 0, 0, 0, 4, 0, 5]
#      [1, 2, 4, 0, 0, 0, 0, 0, 0, 5]
#      [1, 2, 4, 5, 0, 0, 0, 0, 0, 0]


# [0, 1, 0, 3, 12]
#  i  j
# [1, 0, 0, 3, 12]
#     i  j
# [1, 0, 0, 3, 12]
#     i     j
# [1, 3, 0, 0, 12]
#        i  j
# [1, 3, 0, 0, 12]
#        i      j
# [1, 3, 12, 0, 0]

def move_zeroes0(nums):

    if len(nums) == 1:
        return nums
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
            print(nums)
        elif nums[i] == 0 and nums[j] == 0:
            j += 1
        else:
            i += 1
            j += 1
    return nums

# Making it more readable 

def move_zeroes(nums):

    if len(nums) == 1:
        return nums
    
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break

    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums




nums = [8, 2, 0, 0, 0, 0, 1, 5, 0, 4]
print(move_zeroes(nums))