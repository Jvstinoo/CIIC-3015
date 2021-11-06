def WriteDict(dic, f):
    fopen = open(f, 'w')
    for key, value in dic.items():
        fopen.write(f'{key}:{",".join(value)}\n')
    fopen.close()


print(WriteDict({'big': ['dog', 'spam', 'spam'],
      'small': ['cat', 'dog', 'spam']}, 'writeDict.txt'))
