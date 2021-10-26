inp = input('Enter line: ')
pip = 0
out = []
out2 = dict()

for j, i in enumerate(inp):
    if i == ' ':
        out.append(inp[pip:j].strip())
        pip = j
out.append(inp[pip:].strip())

for i in out:
    out2[i] = out.count(i)

print('Most frequent:', max(out2, key=out2.get))
print('Least frequent:', min(out2, key=out2.get))
