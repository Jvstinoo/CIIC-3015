vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def NumVowels(string):
    '''i = 0

    for strings in str:
        for vowel in vowels:
            if(strings == vowel):
                i += 1

    return i'''

    return len([i for i in string if i.lower() in 'aeiou'])


print(NumVowels('prrr'))
print(NumVowels('abcdefghijklmnopqrstuvwxyz'))

print(NumVowels('zzzzzzAaEiIiOuUuzzzzzz'))
print(NumVowels('zzzzzzAaEiIiOuUuzzzzzz'))
