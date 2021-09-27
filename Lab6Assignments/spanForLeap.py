def Span(start_year, start_month, start_day, end_year, end_month, end_day):

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    x_month = days[start_month-1]
    y_month = days[end_month-1]

    counter = 0

    if(start_year > 0):
        difference = x_month - start_day
        total = 0
        for i in days[start_month-1:end_month]:
            total += i - end_day

        return abs(total - difference)


'''
    if(start_year == end_year):
        difference = abs(start_day - x_month)
        diff = abs(end_day - y_month)
        total = difference - diff
        for i in days[start_month:end_month]:
            total += i
    return abs(total)
'''
print(Span(2021, 9, 22, 2021, 9, 22))
print(Span(2021, 9, 22, 2021, 9, 23))
print(Span(2021, 9, 22, 2021, 10, 1))
