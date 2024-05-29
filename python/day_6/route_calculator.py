def is_valid(value):
    if value in ('.0123456789+-*/'):
        return True


def calculate(expression):

    expression = expression.replace('$', '/')
    new = ''
    for e in expression:
        if is_valid(e):
            ...
            

        else:
            return ("400: Bad request")
    return new





print(calculate("5+8-8*2$4"))