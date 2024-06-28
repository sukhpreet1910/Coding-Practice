import sys
def brute_leaders(nums):
    i = 0
    leader_arr = []
    while i < len(nums):
        j = i + 1
        is_leader = True
        while j < len(nums):
            if nums[i] < nums[j]:
                is_leader = False
                break
            j += 1
        if is_leader:
            leader_arr.append(nums[i])
        i += 1

        
    return leader_arr


def optimal_leaders(nums):
    leaders_arr = []
    i = len(nums) - 1
    maxi = float('-inf')
    while i >= 0:
        if nums[i] > maxi:
            leaders_arr.append(nums[i])
            maxi = nums[i]
        i -= 1
    
    return leaders_arr[::-1]


nums = [16,17,4,3,5,2]
leaders_arr = optimal_leaders(nums)
print(leaders_arr)