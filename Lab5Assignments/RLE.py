def RLD(s):
    result = ''
    numbers = []
    letters = []
    n_index = 0
    while(n_index < len(s)):
        numbers.append(int(s[n_index]))
        letters.append(s[n_index+1])
        n_index += 2

    out = 0
    while(out < len(letters)):
        mult = letters[out] * numbers[out]
        result += mult
        out += 1
    return result


print(RLD('3a1B2c1D9e1e'))
print(RLD('1z9Z7Z'))
print(RLD('1A3b1C'))

print(RLD('57'))
print(RLD('1A'))
