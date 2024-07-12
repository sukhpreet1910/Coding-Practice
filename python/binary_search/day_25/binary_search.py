def binary_search(nums, x):
    
    low = 0
    high = len(nums) - 1

    
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            high = mid - 1
        elif nums[mid] < x:
            low = mid + 1


nums = [-1,0,3,5,9,12]
target = 9

indice = binary_search(nums, target)
print(indice)