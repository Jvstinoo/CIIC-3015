'''Write a program that prompts for a DNA string and prints the frequency of each nucleotide (letter in the string).  The output must be in non-ascending order (i.e. from highest lo lowest) by frequency.

Note: You cannot use the key argument for the sort method or for the sorted function.'''

'''inp = input('Enter DNA string: ')

ls = list()

for i in inp:
    if i not in ls:
        ls.append((i, inp.count(i)))
out = [i[1] for i in ]
'''

'''
def s(a, i, j):
    # a is a list
    # 0 ≤ i, j < len(a)
    t = a[i]
    a[i] = a[j]
    a[j] = t
    return a


print(s([1, 2, 3, 4, 5], 1, 2))'''


def Purge(dic, val):
    delete = [dic.pop(i) for i, v in dic.items() if v == val]


F = {(1, 1, 1): 0, (1, 2, 1): 3, (1, 3, 1): 0, (1, 4): 6, (2, 2, 1): 0, (3, 7): 2}
Purge(F, 0)
print(len(F), F[(1, 2, 1)], F[(1, 4)], F[(3, 7)])
