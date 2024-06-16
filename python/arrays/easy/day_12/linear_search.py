def l_search(nums, k):

    for i in range(len(nums)):
        if nums[i] == k:
            return 1
    return -1



nums = [25, 6, 1, 91, 1430]
k = 10
print(l_search(nums, k))