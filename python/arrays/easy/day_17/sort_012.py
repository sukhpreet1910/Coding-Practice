# First Idea i got is, count all the elements using loop
# then loop again insert the required numbers of 0, 1, 2

def counting_sort_colors(nums):
    count0, count1, count2 = 0, 0, 0
    
    for i in nums:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
    
    for i in range(len(nums)):
        if count0 != 0:
            nums[i] = 0
            count0 -= 1
        elif count1 != 0:
            nums[i] = 1
            count1 -= 1
        elif count2 != 0:
            nums[i] = 2
            count2 -= 1
    
    return nums



# Dutch National Flag Algorithm 
# Intuition is: 
#   0 to low-1 are all zeroes
#   low to mid-1 are all ones
#   mid to high this section is unsorted
#   high+1 to n-1 are all twos
# Rule 1: if mid = 0 -> swap(low, mid)
# Rule 2: if mid = 1 -> keep as it is
# Rule 3: if mid = 2 -> swap(mid, high)

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums




nums = [2,0,2,1,1,0]
final = sort_colors(nums)
print(final)