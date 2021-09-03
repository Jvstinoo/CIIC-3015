name, age = (str(input('First name? '))), (int(input('First age? ')))
name2, age2 = (str(input('Second name? '))), (int(input('Second age? ')))


if(age > age2):
    print(name, 'is older')
elif(age2 > age):
    print(name2, 'is older')
else:
    print("It's a tie!")
