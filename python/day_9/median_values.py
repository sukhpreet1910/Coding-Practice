def brute_median_from_n_arrays(arrays):
    new = []
    for i in arrays:
        for j in i:
            new.append(j)
    new = sorted(new)
    mid_index = (len(new) - 1) // 2
    if len(new) % 2 == 0:
        median = (new[mid_index] + new[mid_index + 1]) / 2
    else:
        median = new[mid_index]
    return median



def median_from_n_arrays(arrays):
    ...




arr = [[1,8,10],[2,3,4],[12,20]]
print(median_from_n_arrays(arr))