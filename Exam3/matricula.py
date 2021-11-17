'''Write a function matricula(cournumber) that receives a course number and contains three dictionaries rooms, instructors and times  containing 
course number and the room numbers of the rooms where the courses meet, course number and instructors names, course numbers and time when the class meet.   
You don't need to create the dictionaries. The dictionaries are provided in the code.

Complete the body of the function such as the function  should receive the course number, then it should print the course’s room number, instructor, and meeting time.
 If the course is not found  the function prints course, 'is an invalid course number.'''


def matricula(course):
    # Initialize dictionaries
    rooms = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755,
             'NT110': 1244, 'CM241': 1411}

    instructors = {'CS101': 'Haynes', 'CS102': 'Alvarado',
                   'CS103': 'Rich', 'NT110': 'Burke',
                   'CM241': 'Lee'}

    times = {'CS101': '8:00 am', 'CS102': '9:00 am',
             'CS103': '10:00 am', 'NT110': '11:00 am',
             'CM241': '12:00 pm'}
    # continue writing the function body below
    if course in rooms:
        print(
            f'The details for course {course} are: \nRoom: {rooms[course]} \nInstructor: {instructors[course]} \nTime: {times[course]}')
    else:
        print(f'{course} is an invalid course number.')


matricula('CS101')
