# Brute Force (n^3)

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
# set_zeroes(arr)



# Better Solution O(n^2)



def set_zeros1(arr):
    rows_len = len(arr)
    columns_len = len(arr[0])

    row = [0] * rows_len
    column = [0] * columns_len

    for i in range(rows_len):
          for j in range(columns_len):
               if arr[i][j] == 0:
                    row[i] = 1
                    column[j] = 1
                
    for i in range(rows_len):
        for j in range(columns_len):
             if row[i] or column[j]:
                  arr[i][j] = 0
    print('better', arr)


arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zeros1(arr)


