def removeDuplicates(arr):
    # i = 1

    # while i <= len(nums) - 1:

    #     if nums[i - 1] == nums[i]:
    #         nums.pop(i)  

        
    #     elif nums[i - 1] != nums[i]:
    #         i += 1
    
    # print(nums, len(nums))

    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1
        


nums = [1, 1, 2]
removeDuplicates(nums)