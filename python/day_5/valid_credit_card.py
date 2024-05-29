def validate(n):
    length = len(str(n))

    number = str(n)
    sum = int(number[-1])
    double = True

    for i in range(len(number) - 2, -1, -1):

        digit = int(number[i])

        if double:
            digit *= 2
            double = False
        else:
            double = True

        if digit > 9:
            digit -= 9
        
        sum += digit


    return sum % 10 == 0







validate(1234)