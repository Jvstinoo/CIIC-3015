def Sum(container):
    # recursive function to find sum without using sum()
    if len(container) == 1:
        return container[0]
    else:
        return container[0] + Sum(container[1:])


def NumVowels(string):
    # recursive function to find number of vowels in a string
    if len(string) == 1:
        if string[0] in "aeiouAEIOU":
            return 1
        else:
            return 0
    else:
        if string[0] in "aeiouAEIOU":
            return 1 + NumVowels(string[1:])
        else:
            return NumVowels(string[1:])
