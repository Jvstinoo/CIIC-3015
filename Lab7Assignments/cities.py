'''Write a program that reads a file named cities.txt. Each line in the file contains a number, a comma, and the name of a city. Here are a few lines from the file:

45,Adjuntas
71,Aguada
69,Aguadilla
14,Aguas Buenas
29,Barceloneta
Your program should print the shortest and longest city names.

Note: You should NOT assume that the cities will be cities in Puerto Rico.  You are not interested in the number, only in the names of the cities.

Hint: Remember that a comma is what separates the distance from the city's name.'''

fname = input('Enter file name: ')
fhand = open(fname)

cities = []
result = ''

for line in fhand:
    words = line.split(', ')
    cities.append(words[1])

'''print(cities)
'''

'''        sep = words.split()
'''
print('Shortest city is', min(cities, key=len))
print('Longest city is', max(cities, key=len))

fhand.close()
