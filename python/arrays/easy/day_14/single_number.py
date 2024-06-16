# Brute Force
# count frequency of each element
# store frequencues in a dictionory 
# return element with 1 frequency 
# Note: This solution takes extra space 


def brute_single_number(nums):
    freq = {}

    for i in nums:
        freq[i] = freq.get(i, 0) + 1
    element = [key for key, value in freq.items() if value == 1]
    return element




# Let's try doing it in constant extra space
# XOR Operation 
# Property 1: 1^1 = 0 
# Property 2: 0^1 = 1

def single_number(nums):
    xor = 0
    for i in nums:
        xor = xor ^ i
    return xor


nums = [4,1,2,1,2]
single = single_number(nums)
print(single)