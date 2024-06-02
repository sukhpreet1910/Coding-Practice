def brute_smallest(n):

    # brute force 
    new = n
    num = []
    while new > 0:
        rem = new % 10
        num.append(rem)
        new = new // 10
    num = num[::-1]

    num = [x for x in num if x!= 0]

    minimum = min(num)
    min_index = num.index(minimum)

    num.pop(min_index)

    num.insert(0, minimum)



def brute2_smallest(n):
    
    min_i = 0
    min_j = 0
    str_n = str(n)
    min_n = n


    for i in range(len(str_n)):
        for j in range(len(str_n)):

            if i == j:
                continue

            removing_digit = str_n[i]
            new_n = str_n[:i] + str_n[i+1:]
            new_n = int(str_n[:j] + removing_digit + str_n[j:])

            if new_n < min_n:
                 
                min_n = new_n
                min_i = i
                min_j = j
    removing_digit = int(removing_digit)
    return [min_n, removing_digit, min_j]


def find_min(n):
    return min(n), n.index(min(n))

def smallest(n):
    str_n = str(n)
    count = 0
    for i in range(len(str_n)):
        if count < 1:
            remaining_str = str_n[:i]
            current_str = str_n[i:]
            min_digit, min_index = find_min(current_str)

            if int(current_str[0]) != int(min_digit):
                new_n = int(remaining_str + min_digit + current_str[:min_index] + current_str[min_index + 1:])
                count += 1
        
    return new_n, int(min_digit), int(min_index)




print(smallest(296837))









