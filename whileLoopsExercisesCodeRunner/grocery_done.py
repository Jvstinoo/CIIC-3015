price = input('Price? ')

total = 0

while(price != 'Done'):
    total += float(price)
    price = input('Price? ')
print('Total is $' + str(float(total)))
