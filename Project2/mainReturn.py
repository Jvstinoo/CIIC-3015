def Project2():
    asleep = False
    fed = False
    pantry = False
    flag_tv = False
    safe = False
    key = False
    pantry_opened = False
    bone = False
    spam = True
    get = 'g'
    open = 'o'
    unlock = 'u'
    lock = 'l'
    bed = 'b'
    close = 'c'
    put = 'p'
    tv = 't'
    quit = 'q'
    feed = 'f'
    north = 'n'
    south = 's'
    east = 'e'
    west = 'w'
    turns = 0

    rooms = ['Front Door', 'Living Room', 'Bedroom', 'Office', 'Kitchen']

    cnt_room = 0
    f_room = 0
    l_room = 1
    b_room = 2
    o_room = 3
    k_room = 4

    def living_room():
        print('You enter the living room.')
        if not flag_tv:
            print('The tv is off')
        if flag_tv:
            print('The tv is on.')
        if not fed:
            print('Stella is here, looking hungry and disappointed.')
        else:
            print('The tv is on and Stella is eating her bone.')

    while not asleep:
        print('Location:', rooms[cnt_room])
        inp = input('> ')
        turns += 1

        if inp == quit and not asleep:
            return False

        if cnt_room == f_room:
            if inp == east:
                print(
                    'Home, sweet home! You enter your house.')
                cnt_room = l_room
                living_room()
            continue

        if cnt_room == l_room:
            if inp == east:
                cnt_room = o_room
            if inp == north:
                if not fed:
                    print('Stella refuses to move out of your way. You shall not pass!')
                    continue
                if fed and spam:
                    print("Stella is happily chewing on her nice tasy bone and completely ignores you as you walk into the bedroom. \nYou see a can of lovely spam. Wait, what's that doing in the bedroom? ")
                    cnt_room = b_room
                if fed and not spam:
                    cnt_room = b_room
                continue
            if inp == south:
                print('You enter the kitchen.')
                if not pantry:
                    print('The pantry door is closed.')
                else:
                    print('The pantry door is open.')
                cnt_room = k_room
                continue
            if inp == tv and flag_tv == False:
                print('You turn on the tv.')
                flag_tv = True
                continue
            if inp == tv and flag_tv == True:
                print('You turn off the tv.')
                flag_tv = False
                continue
            if inp == feed and bone == True:
                if flag_tv == True:
                    print('Stella hungrily snatches the nice tasty bone out of your hand and starts to chew on it. She no longer seems to notice or care that you are here.')
                    fed = True
                else:
                    print('Stella seems tense. She keeps glancing from the bone in your hand, to the silent tv, to you, and back to the silent tv again. Every now and then she makes a sad little noise.')
                continue

        if cnt_room == b_room:
            if inp == bed:
                if flag_tv:
                    print('The noise from the tv keeps you awake. ')
                    continue
                if pantry_opened and not flag_tv:
                    print(
                        'You keep thinking about that open pantry door and your OCD stresses you out too much to sleep.')
                    continue
                if pantry and not flag_tv:
                    print(
                        'Wait...did you leave the pantry door unlocked? Better go check.')
                    continue
                if key and not pantry:
                    print(
                        'The pantry in your pocket keeps digging into your leg. Best put it back.')
                    continue
                if safe and not key:
                    print("You're pretty sure you forgot to close the safe.")
                    continue

                if spam and not pantry:
                    print(
                        "You should really put that can of lovely spam away in the pantry first.")
                    continue
                else:
                    print('Sleep! At last! You win!')
                    asleep = True
            if inp == get:
                print("You grab the can of lovely spam.")
                spam = True
                continue
            if inp == south:
                living_room()
                cnt_room = l_room
                continue

        if cnt_room == o_room:
            if inp == west:
                living_room()
                cnt_room = l_room
                continue
            if inp == get and safe:
                print('You remove the pantry door key from the safe.')
                key = True
                continue
            print('You enter your office.')
            if not safe:
                print('The office safe is closed.')
            else:
                print('The office safe is open.')
            if inp == open and not safe:
                print('Please enter the combination to the safe, one number at a time. You remember that it is the next three numbers in the Collatz sequence after 42')
                num1 = int(input('First number? '))
                if num1 == 21:
                    num2 = int(input('Second number? '))
                    if num2 == 64:
                        num3 = int(input('Third number? '))
                        if num3 == 32:
                            print(
                                "You hear a satisfying 'Ka-CHUNK' as the handle turns and the safe door swings invitingly open. \nInside you see the pantry door key")
                            safe = True
                else:
                    print("Nope. that's not it. The locked safe silently mocks you.")
            if inp == put:
                if key and safe:
                    print('You put the pantry door key into the safe.')
                    key = False
                    continue
            if inp == close and safe:
                print('You close the safe and spin the dial a few times to reset it.')
                safe = False
                continue

        if cnt_room == k_room:
            if inp == north:
                living_room()
                cnt_room = l_room
                continue
            if inp == unlock:
                if not key:
                    print("The pantry door is closed. It won't open")
                else:
                    print('You unlock the pantry door.')
                    pantry = True
                continue
            if inp == open and pantry == True:
                print('The pantry door opens. \nInside you see a nice tasty bone.')
                pantry_opened = True
                continue
            if inp == get and pantry_opened:
                print(
                    'You take the nice tasty bone out of the pantry. Stella watches you with great interest from the living room.')
                bone = True
                continue
            if inp == close:
                if pantry:
                    print('The pantry door closes.')
                    pantry_opened = False
                continue
            if inp == lock:
                if pantry_opened == False and key:
                    print('You lock the pantry door.')
                    pantry = False
                continue
            if inp == put and pantry_opened:
                if spam:
                    print(
                        'You put the can of lovely spam into the pantry where it belongs.')
                    spam = False
                continue

    print(turns, 'turns played.')
    return True


print(Project2())
