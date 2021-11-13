def NumVowels(s):
    if len(s) == 0:
        return 0
    if s[0] in 'aeiouAEIOU':
        return NumVowels(s[1:]) + 1
    else:
        return NumVowels(s[1:])


print(NumVowels('spam spam spam'))
print(NumVowels('SpAm EgG sAuSaGe AnD sPaM'))
