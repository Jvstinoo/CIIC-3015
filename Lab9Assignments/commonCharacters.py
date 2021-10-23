def CommonCharacters(string, string2):
    return len(set(string) & set(string2))


print(CommonCharacters('abc', 'xyz'))
print(CommonCharacters('0123456789', '98765431z'))
