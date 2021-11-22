'''Write a function named calc_average that receives student’s grades and then returns their average.  The function should receive as argument a dictionary where the keys are the students’ names and the values are lists of the students’ exam grades.  The function should return a list of 2-item tuples, where the first item is the student’s name and the second item is the average.  The list must be in non-increasing order (largest to smallest) according to the averages.

Example:

gradeDict = dict()

gradeDict[“Petra”] = [90, 80, 100]

gradeDict[“Jose”] = [100, 98, 97, 99]

averageList = calc_average(gradeDict)

# averageList should contain [(“Jose”, 98.5), (“Petra”, 90.0)]'''

'''def calc_average(gradeDict):

    Calculate the average of a dictionary of grades.

    averageList = []
    for student in gradeDict:
        average = sum(gradeDict[student]) / len(gradeDict[student])
        averageList.append((student, average))
    return sorted(averageList, key=lambda x: x[1], reverse=True)

gradeDict = dict()

gradeDict["Petra"] = [90, 80, 100]
'''

'''Write a program that prompts for a DNA string and prints the frequency of each nucleotide (letter in the string).  The output must be in non-ascending order (i.e. from highest lo lowest) by frequency.

Note: You cannot use the key argument for the sort method or for the sorted function.'''

inp = input('Enter DNA string: ')

ls = list()

for i in inp:
    if i not in ls:
        ls.append((i, inp.count(i)))
print(ls)
