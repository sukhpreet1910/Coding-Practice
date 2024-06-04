def removeDuplicates(nums):
    i = 1

    while i <= len(nums) - 1:

        if nums[i - 1] == nums[i]:
            nums.pop(i)  

        
        elif nums[i - 1] != nums[i]:
            i += 1
    
    print(nums, len(nums))
        


nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)