price = input('Price? ')

total = 0.0

nums = [0.0]

while(price != 'Done'):
    total += float(price)
    nums.append(float(price))
    price = input('Price? ')

print('Total is $' + str(total))
nums.sort()
print('The largest entered price is $' + str(nums[-1]))
