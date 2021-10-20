def AlmostPrint(*sep):
    for i in sep:
        if len(sep) > 1:
            print(sep[0][:] + str(sep[1]))
            break


AlmostPrint('string', 'pop')
AlmostPrint('hello', 'world', sep=', ')
