# Unsolved 


def lcs(x, y):
    x_len = len(x)
    y_len = len(y)

    freq = {}
    new = ''

    for c in x:
        freq[c] = freq.get(c, 0) + 1

    i, j = 0, 0
    while i < x_len and j < y_len:
        
        if y[j] in freq and freq[x[i]] > 0:
            if x[i] == y[j]:
                freq[x[i]] = freq[x[i]] - 1
                new = new + y[j]
                i += 1
                j += 1
                
            else:
                freq[x[i]] = freq[x[i]] - 1
                i += 1
        else:
            j += 1
            i += 1
    print(new)



lcs("anothertest", "notatest") # nottest


# # lcs("finaltest", "zzzfinallyzzz")  # "final"