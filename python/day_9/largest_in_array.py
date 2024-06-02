arr = [4, 2, 6, 0, 9, 10, 1, 5, 20]

def optimal_largest( arr, n):                          # Optimal 
    maximum = arr[0]
    for i in range(n):
        if arr[i] > maximum:
            maximum = arr[i]
    print(maximum)
        
optimal_largest(arr, len(arr))




def brute_largest(arr, n):                            # Brute 
    arr = sorted(arr)
    print(arr[n-1])

brute_largest(arr, len(arr))