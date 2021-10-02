def Span(start_year, start_month, start_day, end_year, end_month, end_day):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    x_month = days[start_month-1]
    y_month = days[end_month-1]

    leap_years = []
    for i in range(1000, 6000, 4):
        if(i % 100 == 0 and i % 400 == 0):
            leap_years.append(i)
        elif(i % 400 == 0 or i % 4 == 0) and not(i % 100 == 0):
            leap_years.append(i)

    counter = 0

    if(start_year > 0) and (start_month <= end_month):
        difference = abs(start_day - x_month)
        diff = abs(end_day - y_month)
        total = difference - diff
        for i in days[start_month:end_month]:
            total += i
        for i in range(start_year, end_year):
            counter += 365
            if(i in leap_years) and (i != start_year):
                counter += 1
        if(start_year in leap_years) and (start_month <= 2) or (end_year in leap_years and end_month >= 2):
            counter += 1

        return abs(total + counter)

    elif(start_month > end_month):
        mew = []
        difference = abs(start_day - x_month)
        total = difference + end_day
        for i in days[start_month:]:
            counter += i

        for j in days[0:end_month-1]:
            total += j
        for k in range(start_year, end_year):
            if(end_year - start_year != 1):
                counter += 365
                if(k in leap_years) and (k != start_year):
                    counter += 1
        if(start_year in leap_years) and (start_month <= 2) or (end_year in leap_years and end_month >= 2):
            counter += 1
        elif(end_year - start_year != 1):
            counter -= 365
        return abs(total + counter)


print(Span(1599, 12, 31, 2021, 9, 22))  # 154033

print(Span(1966, 12, 4, 1989, 10, 28))  # 8364


print(Span(2021, 9, 22, 2022, 1, 1))  # 101
print(Span(1962, 2, 11, 1966, 12, 4))  # 1757
