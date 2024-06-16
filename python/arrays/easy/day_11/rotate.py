
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

def brute_rotate(arr, k):           

    n = len(arr)
    k = k % n

    rotate_index = n - k
    i = 0
    while rotate_index > 0:
        arr.append(arr[i])
        arr.pop(i)
        rotate_index -= 1
    
    print(arr)

# brute_rotate(nums, k)


def brute2_rotate(arr, k):           

    n = len(arr)
    k = k % n

    rotate_index = n - k
    print(rotate_index)
    arr = arr[rotate_index:] + arr[:rotate_index]
    
    print(arr)

# brute2_rotate(nums, k)



#  [1, 2, 3, 4, 5, 6, 7]
#  [4, 3, 2, 1, 5, 6, 7]
#  [4, 3, 2, 1, 7, 6, 5]
#  [5, 6, 7, 1, 2, 3, 4]
def optimal_rotate(arr, k):

    n = len(arr)
    k = k % n
    rotate_index = n - k

    arr[:rotate_index] = reversed(arr[:rotate_index])

    arr[rotate_index:] = reversed(arr[rotate_index:])

    arr[:] = reversed(arr)

    print(arr)

optimal_rotate(nums, k)
