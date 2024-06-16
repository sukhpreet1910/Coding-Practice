# First logic comming to my mind is 2 pointer 
# start left right both from first 
# increasing both until you got target 

def less_opt_two_sum(nums, target):
    left, right = 0, 1

    while right < len(nums) and left != right:
        sum = 0
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        
        
        if right == len(nums) - 1:
            left += 1
            right = left + 1
        right += 1


# Variation in two pointer approach if you just need to return if indicies are present or not 
def better_two_sum(nums, target):

    nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return 'Yes'
        
        elif sum < target:
            left += 1
        else:
            right -= 1
    return 'No'


# If we need to return indicies, then we will use hashing
# Subtract current element from target and look if the result of subtraction present in hashmap
# return indices

def two_sum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        if difference in hashmap:
            return [i, hashmap[difference]]
        
        hashmap[nums[i]] = i


nums = [3,2,4]
target = 6
indicies = two_sum(nums, target)
print(indicies)
