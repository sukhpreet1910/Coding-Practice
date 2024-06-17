# First solution came to mind is using hashing 
# pseado code 
# 1.count freq of each element
# 2.convert list into set to get unique elements
# 3.loop through set and check freq in hashset along side.
# 4.return majority element 

def majority_element(nums):
    hashset = {}

    for i in nums:
        hashset[i] = hashset.get(i, 0) + 1

    maj_element = len(nums) // 2
    for key, value in hashset.items():
        if value >= maj_element:
            return key
        
# Complexity Analysis 
# Time Complexity :
    # Insertion in the hashset takes O(1)
    # O(n) for array travserval 
    # so, its time complexity is O(n) 
# Space Complexity 
    # O(n)


    

# Moore's voting algorithm 
    # pick first element as the current element
    # check if next element is same as current element 
        # count++
    # if next element is not same
        # count--
    # if count == 0
        # change make next element the current element
    # at the end of the traversal if count is not zero take that element and 
    # check if it's count is more than majority element count 


def moore_algo(nums):

    count, element = 0, 0

    for i in range(len(nums)):
        if count == 0:
            count = 1
            element = nums[i]
        elif element == nums[i]:
            count += 1
        else:
            count -= 1


    # if its not given than element is present for sure 
    maj_elem = len(nums) // 2
    actual_count = 0
    for i in nums:
        if i == element:
            actual_count += 1
    
    if actual_count > maj_elem:
        return element
    
    return - 1
        


nums = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 1, 1, 1, 1]
element = moore_algo(nums)
print(element)