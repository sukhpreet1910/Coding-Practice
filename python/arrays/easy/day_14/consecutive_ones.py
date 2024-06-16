# Brute Method 
# Loop through list 
# if current position is 1
#    if 1, check next and keep checking until another element comes up
#    if another element comes up, make count 0 again
# Compare max_count and count

def ones(nums):
    count = 0
    max_count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        
        max_count = max(max_count, count)
    
    return max_count

nums = [1, 1, 0, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 0]
ones = ones(nums)
print(ones)