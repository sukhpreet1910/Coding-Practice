def rot13(message):

    # empty string to store resulting string 
    # iterate over the given string 
    # check if current character is an alphabet
        # if yes add 13 ascii letters to transform or rotate it 
         # append it into resulting string
        # else
         # Append the value 
    # return resulting string 

    # 65-90 to A-Z
    # 97-122 to a-z
    
    new = ''

    for m in message:

        if m.isalpha():
            ascii = ord(m)
            if ascii >= 65 and ascii <= 90:
                ascii = (((ascii - 65) + 13) % 26) + 65
            elif ascii >= 97 and ascii <= 122:
                ascii = (((ascii - 97) + 13) % 26) + 97
            new = new + chr(ascii)
        else:
            new = new + m

    return new


print(rot13("EBG13 rknzcyr."))