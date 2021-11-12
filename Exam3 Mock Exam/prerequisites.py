# Test files stored in Moodle server
fname = input('Enter file name: ')
fopen = open(fname)

out = {}

for lines in fopen:
    n = lines.strip().split(',')[0]
    if n in out:
        out[n] += 1
    else:
        out[n] = 1
print('Course Number of Requisites')
for key, value in out.items():
    print(key, value)

fopen.close()
### ADD CODE TO PRINT HERE ###
# Separate fields with a space
