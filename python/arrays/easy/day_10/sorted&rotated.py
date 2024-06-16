# Check how many times a ith element is less than i - 1 element


def check(nums):
        count = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                    count += 1
        
        if nums[len(nums) - 1] > nums[0]:
               count += 1
            
        
        return count == 1



nums = [2, 7, 4, 1, 2, 6, 2]
print(check(nums))



