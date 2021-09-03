# Check if year is a leap year

def IsLeapYear(n):
    if(n % 100 == 0 and n % 400 == 0):
        return True
    elif(n % 400 == 0 or n % 4 == 0) and not(n % 100 == 0):
        return True
    return False


print(IsLeapYear(2000))
print(IsLeapYear(2021))
print(IsLeapYear(2024))
print(IsLeapYear(2100))
