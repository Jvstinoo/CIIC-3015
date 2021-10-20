def ToRoman(n):
    values = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    counter = 0
    out = ''

    while counter <= n:
        for i in range(n):
            for j in values:
                if j <= n and counter < n:
                    out += values[j]
        counter += 1
    return
