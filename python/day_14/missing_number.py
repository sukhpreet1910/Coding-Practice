# Brute Force 
# 1. Sort the array
# 2. Run the loop through the range
# 3. simpy check at the iteration if element is present in array

def brute_missing_number(nums):
    nums = sorted(nums)
    n = len(nums)

    j = 0
    for i in range(0, n + 1):
        if i != nums[j]:
            return i
        if j < n - 1:
            j += 1



# Better Approach 
# Count Frequencies of all in the range
# return the number with 0 frequency  

def better_missing_value(a):
    N = len(nums)
    hash = [0] * (N + 1)  # hash array

    # storing the frequencies:
    for i in range(N - 1):
        hash[a[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1                   



# optimal 
# Sum all the numbers from 0 to length of the array
# Sum all the numbers of array
# Subtract Both


def missing_number(nums):
    
    # sum = 0
    # arr_sum = 0
    # for i in range(0, len(nums) + 1):
    #     sum = sum + i
    #     if i < len(nums):
    #         arr_sum += nums[i]

    # return sum - arr_sum


    # making my code better
    n = len(nums)
    total_sum = (n * (n + 1)) // 2

    arr_sum = sum(nums)

    return total_sum - arr_sum

nums = [0,1]
miss = missing_number(nums)
print(miss)