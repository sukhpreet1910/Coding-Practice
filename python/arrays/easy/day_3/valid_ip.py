# 6 KYU: https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python 

def is_valid_IP(strng):
    octets = strng.split('.')

    # check for white space at the end 
    # check if octet start with 0 if length of octet is greater than 1 
    # check if it is contains alphabets 
    # check for 0 - 255 if digit

    if len(octets) != 4:
        return False
    
    count = 0
    space = False 
    zero = False
    for o in octets:
        if o.endswith(' '):
            space = True 
        if len(o) > 1 and o.startswith('0'):
            zero = True 
        if o.isdigit():
            if not space and not zero and 0 <= int(o) <= 255:
                count += 1
    if count != 4:
        return False
    
    return True 


print(is_valid_IP('a1.255.056.1'))