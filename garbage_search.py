def F(string, string2):
    return (string2 in ''.join([i for i in string if i in string2]))


print(F('a!b!c', 'abc'))
print(F('azozbaz', 'zz'))
print(F('abc', 'cba'))
