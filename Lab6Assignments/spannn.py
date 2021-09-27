def Span(start_year, start_month, start_day, end_year, end_month, end_day):
    start_month -= 1
    end_month -= 1

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start_month = days[start_month]
    end_month = days[end_month]

    counter = 0

    leap_years = []
    for i in range(1000, 6000, 4):
        leap_years.append(i)

    if(start_year in leap_years):

        diferencia = start_month - start_day + 1
        total = end_day + diferencia
        for i in days[start_month-1:end_month]:
            total += i

        return total, diferencia


print(Span(2020, 2, 28, 2020, 5, 1))


'''
    if(start_year > 0):
        difference = abs(start_day - x_month)
        diff = abs(end_day - y_month)
        total = difference - diff
        for i in days[start_month:end_month]:
            total += i
        for i in range(start_year, end_year):
            counter += 365

        return abs(total + counter)'''


print(Span(1966, 12, 4, 1989, 10, 28))
