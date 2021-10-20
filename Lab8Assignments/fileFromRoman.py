values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def FromRoman(s):
    out = []

    for i in s:
        out.append(values[i])

    if len(out) > 1:
        for index, i in enumerate(out):
            try:
                if i < out[index+1]:
                    out[index+1] = out[index+1] - i
                    out.remove(i)

            except:
                pass

    return sum(out)


def FileFromRoman(file, newFile):
    fhand = open(file)
    fhand2 = open(newFile, 'w')
    end = '\n'

    for line in fhand:
        fhand2.write(str(FromRoman(line.strip()))+end)

    fhand.close()
    fhand2.close()

    f = open(newFile, "r")
    print(f.read())


print(FileFromRoman('nums.txt', 'newfile.txt'))
