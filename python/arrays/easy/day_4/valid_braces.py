def opening_brace(brace):
    return (brace == '(' or brace == '[' or brace == '{')


def valid_braces(string):
    
    brace_stack = []

    for s in string:
        brace = s

        if opening_brace(brace):
            brace_stack.append(brace)

        else:
            last_brace = brace_stack.pop()
            if last_brace == '(' and brace != ')':
                return False
            elif last_brace == '[' and brace != ']':
                return False
            elif last_brace == '{' and brace != '}':
                return False
        
    if len(brace_stack) != 0:
        return False
    else:
        return True 
            


print(valid_braces("(({{[[]])"))
# ()