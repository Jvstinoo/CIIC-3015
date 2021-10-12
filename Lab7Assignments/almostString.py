def AlmostPrint(args, *sep):
    output = ''
    out = ''

    if sep != None:

        for k in args:
            out += k + str(sep)
        return out

    for i in args:
        output += i + ' '
    return output


print(AlmostPrint('hello', 'world'))
print(AlmostPrint('hello', 'world', sep=', '))
