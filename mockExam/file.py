fname = input('Enter file name: ')
fhand = open(fname)
str = 'X-DSPAM-Confidence:'
out = []

for line in fhand:
    if str in line:
        out.append(float(line.split(':')[1].strip()))
print(out)
print('Largest spam confidence:', max(out))
print('Number of times:', out.count(max(out)))
