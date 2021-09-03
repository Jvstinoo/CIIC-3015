def Vacation(name, months):
    year = months//12

    if name == 'Facebook':
        return 20
    elif name == 'Amazon':
        if(year > 1):
            return 15
        return 10
    elif name == 'Google':
        if(year >= 5):
            return 25
        if(year >= 3):
            return 20
        return 15

    elif name == 'Apple':
        if(year >= 3):
            return 15
        if(year == 5):
            return 17
        if(year >= 4):
            return (15 + year-3)

        return 12

    elif name == 'Microsoft':
        if(year == 5):
            return 20
        if(year >= 5):
            if(int((15 + (year * 1.5))//1) >= 30):
                return 30

        return 15


print(Vacation('Microsoft', 84))

print(Vacation('Apple', 37))
print(Vacation('Google', 36))
print(Vacation('Facebook', 100))

print(Vacation('Amazon', 36))
print(Vacation('Apple', 60))
print(Vacation('Microsoft', 1000))
