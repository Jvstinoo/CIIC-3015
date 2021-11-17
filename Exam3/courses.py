'''Write a program to read each line of a file that contains information about the courses in the following format: course number:rooms where the 
courses meet, meeting time, instructor name. 

Here are some examples of the lines of the file :


CIIC4015:s121,8:00 am,Velez
INSO4020:s113,9:00 am,Balaguera
CIIC3015:s114,15:30 pm,Sierra
CIIC4035:s121,10:00 am,Rodriguez
INSO4035:s121,12:00 pm,Rivera
CIIC5011:s201,17:00 pm,Arzuaga
Create and print a dictionary containing course numbers (keys) and the numbers of the rooms where the courses meet (values).'''

inp = input('Enter file name: ')
fopen = open(inp)
out = dict()

for lines in fopen:
    colon = lines.find(':')
    comma = lines.find(',')
    out[lines.split(':')[0]] = lines[colon+1:comma]
fopen.close()
print(out)
