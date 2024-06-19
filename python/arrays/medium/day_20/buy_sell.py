def max_profit(nums):
    profit = 0
    i, j= 0, len(nums) - 1
    sell, buy= 0, 1

    while i < j:

        if nums[buy] > nums[sell]:
            buy = sell
            sell += 1
        
        else:
            profit = max(nums[sell] - nums[buy], profit)
            sell += 1

        i += 1
    
    return profit









prices = [7,1,5,3,6,4]
profit = max_profit(prices)
print(profit)