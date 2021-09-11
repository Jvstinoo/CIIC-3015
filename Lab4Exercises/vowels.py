vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def NumVowels(str):
    i = 0

    for strings in str:
        for vowel in vowels:
            if(strings == vowel):
                i += 1

    return i


print(NumVowels('prrr'))
print(NumVowels('abcdefghijklmnopqrstuvwxyz'))

print(NumVowels('zzzzzzAaEiIiOuUuzzzzzz'))
