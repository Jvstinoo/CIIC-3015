values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def FromRoman(s):
    out = []

    for i in s:
        out.append(values[i])

    if len(out) > 1:
        for index, i in enumerate(out):
            try:
                if i < out[index+1]:
                    out[index+1] = out[index+1] - i
                    out.remove(i)

            except:
                pass

    return sum(out)


print(FromRoman('CDXCIV'))

print(FromRoman('CCCXCIX'))

print(FromRoman('I'))
print(FromRoman('II'))
print(FromRoman('VI'))
print(FromRoman('IX'))
print(FromRoman('MCMLXVI'))
