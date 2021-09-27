def Span(start_year, start_month, start_day, end_year, end_month, end_day):

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    x_month = days[start_month-1]
    y_month = days[end_month-1]

    # Generate list of Leap Years
    leap_years = []
    for i in range(1000, 6000, 4):
        leap_years.append(i)

    # If start or end year is a leap year change its shit
    if(start_year in leap_years):
        start_year = 366
        days[1] = 29
    if(end_year in leap_years):
        end_year = 366
        days[1] = 29

    if(start_year == end_year):
        difference = abs(start_day - x_month)
        diff = abs(end_day - y_month)
        total = difference - diff
        for i in days[start_month:end_month]:
            total += i
        return abs(total)


print(Span(2021, 9, 22, 2021, 9, 22))

print(Span(2021, 9, 22, 2021, 9, 23))

print(Span(2021, 9, 22, 2021, 10, 1))
print(Span(2021, 9, 22, 2021, 12, 31))

print(Span(2021, 9, 22, 2022, 1, 1))

print(Span(2021, 9, 22, 2022, 9, 22))

print(Span(2021, 2, 28, 2021, 3, 1))

print(Span(2020, 2, 28, 2020, 3, 1))

print(Span(1962, 2, 11, 1966, 12, 4))

print(Span(1966, 12, 4, 1989, 10, 28))

print(Span(1989, 10, 28, 1993, 7, 23))

print(Span(1993, 7, 23, 1998, 6, 20))

print(Span(1998, 6, 20, 2006, 7, 21))

print(Span(2006, 7, 21, 2011, 6, 22))

print(Span(2011, 6, 22, 2014, 4, 7))

print(Span(2014, 4, 7, 2019, 3, 4))

print(Span(2019, 3, 4, 2020, 8, 29))

print(Span(2020, 8, 29, 2021, 8, 10))

print(Span(1966, 12, 4, 2021, 9, 6))
print(Span(1599, 12, 31, 2021, 9, 22))


'''    if(start_year % 100 == 0 and start_year %400 == 0) or (start_year % 400 == 0 or start_year % 4 == 0) and not(start_year % 100 == 0):
        days[1] = 29
        year = 366

'''
