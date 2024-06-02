arr = [10, 5, 10]

def brute_second_largest(arr):          # O(nlogn), This works if there are no duplicates

    arr = sorted(arr)
    print(arr[len(arr)-2])

brute_second_largest(arr)


def better_second_largest(arr):

    n = len(arr)
    largest = arr[0]
    for i in range(n):
        largest = max(arr[i], largest)
    
    second_largest = arr[0]
    for i in range(n):
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    print(second_largest)

better_second_largest(arr)


def optimal_second_largest(arr):

    if len(arr) < 2:
        return -1
    
    largest = float('-inf')
    second_largest = float('-inf')

    for i in range(len(arr)):

        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    if second_largest == float('-inf'):
        return - 1
    else:
        return second_largest


optimal_second_largest(arr)








