# Using Kadane's algo

def maximum_subarray(nums):
    sum = 0
    maximum_sum = nums[0]
    for i in nums:
        sum += i
        if sum > maximum_sum:
            maximum_sum = max(maximum_sum, sum)
        if sum < 0:
            sum = 0
            continue
        
    return maximum_sum



# Also print the subarray

def print_maximum_subarray(nums):
    sum = 0
    maximum_sum = nums[0]

    ans_start, ans_end = -1, -1

    for i in range(len(nums)):

        if sum == 0:
            start = i
        sum += nums[i]
        if maximum_sum < sum:
            maximum_sum = sum
            ans_start = start
            ans_end = i
        if sum < 0:
            sum = 0
    
    return nums[ans_start:ans_end + 1]


nums = [-2,1,-3,4,-1,2,1,-5,4]

sum = print_maximum_subarray(nums)
print(sum)