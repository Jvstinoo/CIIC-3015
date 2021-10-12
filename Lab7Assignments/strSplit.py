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
    choice = 0
    turns = 0

    rooms = ['Front Door', 'Living Room', 'Kitchen', 'Office', 'Bedroom']
    tv, pantry, office, asleep, bone, safe, key = False, False, False, False, False, False, False
    print('What an awful day! You are completely exhausted, all you want to do is climb into bed and collapse... \nCIIC 3015 Autumn 2021 Project 2: The Quest for Sleep\n')

    while not asleep:
        print('Current Location:', rooms[choice])

        selection = input('> ')
        if selection == quit:
          return False

        if selection == east and choice == 0:
          print('Home, sweet home! You enter your house. \nYou enter the living room. \nThe tv is off. \nStella is here, looking hungry and disappointed.')
          choice = 1
          

        
        elif selection == south and choice == 1:
          print('You enter the kitchen. \nThe pantry is closed.')
          choice = 2
          

        elif selection == east and choice == 1:
          print('You enter the office. \nThe safe is closed.')
          choice = 3
        elif selection == open and choice == 3:
            print('Please enter the combination to the safe, one number at a time. \nYou remember that it is the next three numbers in the Collatz sequence after 42.')
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
                print('You hear a satisfying sound as the door to the safe slowly opens. \nInside you see the pantry door key.')
                asleep = True
            else:
              print("Nope, that's not it")
              continue
        
        
        if selection == open and choice == 2:
          print("The pantry door is closed. It won't open.")
    print("Sleep! At last! You win!")
    print(turns, 'turns played')

Project2()