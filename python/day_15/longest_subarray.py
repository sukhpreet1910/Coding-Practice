# subarray: contiguous part of the array

# Two pointer Approach
def longest_subarray(arr, k):
    left, right = 0, 0
    sum = arr[0]
    max_length = 0

    while right < len(arr):

        while left <= right and sum > k:
            sum -= arr[left]
            left += 1

        if sum == k:
            max_length = max(max_length, right - left + 1)

        right += 1
        if right < len(arr):
            sum += arr[right]

    return max_length

        




arr = [1, 2, 3, 1, 1, 1, 1, 3, 3]
k = 3
sub = longest_subarray(arr, k)
print(sub)