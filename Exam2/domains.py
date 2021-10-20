fname = input('Enter file name: ')
fhand = open(fname, 'r')
out = []

for line in fhand:
    if 'From:' in line:
        nl = line.split('@')[1].strip()
        out.append(nl.split(' ')[0])
print('Shortest domain is:', min(out, key=len))
print('Longest domain is:', max(out, key=len))

fhand.close()
