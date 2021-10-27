def DoIWin(path):
    fhand = open(path, 'r')
    read = fhand.readlines()
    out = [[], [], [], [], [], [], [], [], []]
    colCheck = True
    rowCheck = True
    squareCheck = True

    for i, lineas in enumerate(read):
        for j, chars in enumerate(lineas.strip()):
            out[j].append(chars)

    for index, val in enumerate(out):
        if len(set(out[index])) == 9:
            pass
        else:
            rowCheck = False
            break
    fhand.seek(0)
    for lines in fhand:
        if len(set(lines.strip())) == 9:
            pass
        else:
            colCheck = False
            break
    fhand.seek(0)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = read[i][j:j + 3] + \
                read[i + 1][j:j + 3] + read[i + 2][j:j + 3]
            if len(set(nums)) == 9:
                pass
            else:
                squareCheck = False
                break
    fhand.seek(0)
    if squareCheck and rowCheck and colCheck:
        return True
    else:
        return False

    fhand.close()


print(DoIWin('sudoku.txt'))
