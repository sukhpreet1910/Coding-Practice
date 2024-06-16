import math
# count numbers 
# count prime 
# count divisors 
def prime_check(n):

    if n <= 1:
        return False
    
    if n <= 3:
        return True 
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


def divisors(i):

    div = 0
    for d in range(1, int(math.sqrt(i) + 1)):
        if i % d == 0:
            div += 1
            if d != i // d:
                div += 1
    return div


def proc_arr_int(lst):

    count = len(lst)
    prime_count = sum(1 for i in lst if prime_check(i))


    hash = {i : divisors(i) for i in lst}
    max_value = max(hash.values())
    max_keys = sorted([key for key, value in hash.items() if value == max_value])


    nested = [max_value, max_keys]
    info = [count, prime_count, nested]

    return info





arr1 = [267, 273, 271, 145, 275, 150, 487, 169, 428, 50, 314, 444, 445, 67, 458, 211, 58, 95, 357, 486, 359, 491, 108, 493, 247, 379]

proc_arr_int(arr1)