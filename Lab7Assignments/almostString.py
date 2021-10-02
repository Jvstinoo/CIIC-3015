def AlmostPrint(*args):
    output = ''

    for i in args:
        output += i + ' '
    return output


print(AlmostPrint('hello', 'world'))
