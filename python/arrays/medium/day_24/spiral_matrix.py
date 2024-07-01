# Brute Force Pseudo Code 
# 


def spiral(nums):
    
    ans = []
    row = len(nums)
    col = len(nums[0])
    
    top = 0
    left = 0
    right = col - 1
    bottom = row - 1

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            ans.append(nums[left][i])
        
        top += 1

        for i in range(top, bottom + 1):
            ans.append(nums[i][right])

        right -= 1


        for i in range(right, left - 1, -1):
            ans.append(nums[bottom][i])

        bottom -=1

        for i in range(bottom, top - 1, - 1):
            ans.append(nums[i][left])

        left += 1

    return ans

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiral_matrix = spiral(nums)
print(spiral_matrix)

[1,2,3,4],
[5,6,7,8],
[9,10,11,12]