def upper_vs_lower(s):
    lower = 0
    upper = 0

    for i in s:
        if i.isupper() and i.isalpha():
            upper += 1
        if i.islower() and i.isalpha():
            lower += 1

    if lower < upper:
        print('Upper wins')
    if upper < lower:
        print('Lower wins')
    elif lower == upper:
        print('Tie')


upper_vs_lower('iPhone 11')
upper_vs_lower('GRCh38')
