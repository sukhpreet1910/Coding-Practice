def brute_union(arr1, arr2):
    n = max(len(arr1), len(arr2))
    temp = []
    for i in range(len(arr1)):
        if arr1[i] not in temp:
            temp.append(arr1[i])
        if arr2[i] not in temp:
            temp.append(arr2[i])
        
    
    print(temp)



def union(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i, j = 0, 0
    temp = []
    while i <= n-1 and j <= m-1:

        if arr1[i] <= arr2[j]:
            if len(temp) == 0 or temp[-1] != arr1[i]:
                temp.append(arr1[i])
            i += 1

        elif arr1[i] >= arr2[j]:
            if len(temp) == 0 or temp[-1] != arr2[j]:
                temp.append(arr2[j])
            j += 1


    
    while i <= n - 1:
        if temp[-1] != arr1[i]:
            temp.append(arr1[i])
        i += 1

    while j <= m-1:
        if temp[-1] != arr2[j]:
            temp.append(arr2[j])
        j += 1
        
    print(temp)

            





arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 6, 7, 10, 20, 30, 40, 50]

union(arr1, arr2)
