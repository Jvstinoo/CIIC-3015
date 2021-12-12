# Check if year is a leap year

def IsLeapYear(n):
    # New solution
    return ((n % 4 == 0 and not n % 100 == 0) or (n % 400 == 0 and n % 100 == 0))
    # Old solution
    '''if(n % 100 == 0 and n % 400 == 0):
        return True
    elif(n % 400 == 0 or n % 4 == 0) and not(n % 100 == 0):
        return True
    return False'''


print(IsLeapYear(2000))
print(IsLeapYear(2021))
print(IsLeapYear(2024))
print(IsLeapYear(2100))
print(IsLeapYear(1966))
print(IsLeapYear(1980))
