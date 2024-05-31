def set_zeroes(arr):
    flag = True
    index = []
    for i in arr:
        for j in range(len(i)):
            if i[j] == 0:
                    index.append(j)
        for j in range(len(i)):
            if i[j] == 0:
                i[:] = [0] * len(i)

    for i in arr:
        for j in index:
            i[j] = 0

    print(arr)

arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zeroes(arr)