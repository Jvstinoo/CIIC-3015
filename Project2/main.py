def Project2():
    bed = 'b'
    close = 'c'
    east = 'e'
    feed = 'f'
    get = 'g'
    lock = 'l'
    north = 'n'
    open = 'o'
    put = 'p'
    quit = 'q'
    south = 's'
    tv = 't'
    unlock = 'u'
    west = 'w'

    cnt_room = 0
    front_door = 0
    living_room = 1
    bedroom = 2
    office = 3
    kitchen = 4

    turns = 0

    rooms = ['Front Door', 'Living Room', 'Bedroom', 'Office', 'Kitchen']
    tv, pantry, office, asleep, bone, safe, key, fed = False, False, False, False, False, False, False, False
    print('What an awful day! You are completely exhausted, all you want to do is climb into bed and collapse... \nCIIC 3015 Autumn 2021 Project 2: The Quest for Sleep\n')

    while not asleep:
        print('Current Location:', rooms[cnt_room])
        selection = input('> ')

        if selection == east and cnt_room == front_door:
            print('Home, sweet home! You enter your house. \nYou enter the living room.')
            cnt_room = living_room
            turns += 1

        elif selection == north and cnt_room == living_room:
            if not fed:
                print('Stella refuses to move out of your way. You shall not pass!')

        elif selection == east and cnt_room == living_room:
            print('You enter the office. \nThe safe is closed.')
            cnt_room = office
            turns += 1
            continue

        elif selection == open and cnt_room == office:
            print('Please enter the combination to the safe, one number at a time. \nYou remember that it is the next three numbers in the Collatz sequence after 42.')
            turns += 1
            num1 = int(input('First number? '))
            if num1 == 21:
                num2 = int(input('Second number? '))
            else:
                print("Nope that's not it.")
                continue
            if num2 == 64:
                num3 = int(input('Third number? '))
            else:
                print("Nope that's not it.")
                continue
            if num3 == 32:
                print(
                    'You hear a satisfying sound as the door to the safe slowly opens. \nInside you see the pantry door key.')
                safe == True
            else:
                print("Nope, that's not it")
                continue
        elif selection == get and cnt_room == office and safe == True:
            print('You remove the pantry door key from the safe.')
            key == True
        elif selection == west and cnt_room == office:
            cnt_room = living_room

        elif selection == south and cnt_room == living_room:
            print('You enter the kitchen. \nThe pantry is closed.')
            cnt_room = kitchen
            turns += 1

        if selection == open and cnt_room == kitchen:
            print("The pantry door is closed. It won't open.")
            turns += 1

        elif selection == quit:
            return False
    print("Sleep! At last! You win!")
    print(turns, 'turns played')


Project2()
