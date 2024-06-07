def brute_union(arr1, arr2):
    s = set()
    union = []

    for nums in arr1:
        s.add(nums)

    for nums in arr2:
        s.add(nums)
    
    for nums in s:
        union.append(nums)

    return union
    



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

            





arr1 = [-7, 8]
arr2 = [-8, -3, 8]

print(brute_union(arr1, arr2))
