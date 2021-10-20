times = int(input('How many numbers will be entered? '))

out = []

for i in range(times):
    num = input('Enter number: ')
    out.append(int(num))

print(sum(out)/len(out))
