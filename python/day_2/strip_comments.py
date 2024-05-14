def strip_comments(strng, markers):
    lines = strng.split('\n')
    
    new = []
    for l in lines:
        word = ''
        for c in l:
            if c in markers:
                break
            else:
                word = word + c
        new.append(word)

    return '\n'.join(new)





strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])