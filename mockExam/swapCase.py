def swap_case(str):
    out = ''

    for j, i in enumerate(str):
        if i.isupper() and i.isalpha():
            out += str[j].lower()
        if i.islower() and i.isalpha():
            out += str[j].upper()
        elif i.isalpha() == False:
            out += str[j]

    return out


print(swap_case('ThisString'))

print(swap_case('iPhone 11'))
