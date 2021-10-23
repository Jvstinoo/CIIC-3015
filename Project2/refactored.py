def Project2():
    bools = {'asleep': False, 'fed': False, 'pantry': False, 'flag_tv': False, 'safe': False,
             'key': False, 'pantry_opened': False, 'bone': False, 'spam': False, 'spam_stored': False}
    inputs = {'get': 'g', 'open': 'o', 'unlock': 'u', 'lock': 'l', 'bed': 'b', 'close': 'c', 'put': 'p',
              'tv': 't', 'quit': 'q', 'feed': 'f', 'north': 'n', 'south': 's', 'east': 'e', 'west': 'w'}

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
        if not bools['flag_tv']:
            print('The tv is off')
        if bools['flag_tv']:
            print('The tv is on.')
        if not bools['fed']:
            print('Stella is here, looking hungry and disappointed.')
        else:
            print('Stella is here, happily chewing on her nice tasty bone. ')

    while not bools['asleep']:
        print('Location:', rooms[cnt_room])
        inp = input('> ')
        turns += 1

        if inp not in inputs.values():
            print('Invalid choice :(')

        if inp == inputs['quit'] and not bools['asleep']:
            return False

        if cnt_room == f_room:
            if inp == inputs['east']:
                print(
                    'Home, sweet home! You enter your house.')
                cnt_room = l_room
                living_room()
            continue

        if cnt_room == l_room:
            if inp == inputs['east']:
                print('You enter your office.')
                if not bools['safe']:
                    print('The office safe is closed.')
                else:
                    print('The office safe is open.')
                cnt_room = o_room
                continue
            if inp == inputs['north']:
                if not bools['fed']:
                    print('Stella refuses to move out of your way. You shall not pass!')
                    continue
                if bools['fed'] and not bools['spam']:
                    print("Stella is happily chewing on her nice tasty bone and completely ignores you as you walk into the bedroom. \nYou see a can of lovely spam. Wait, what's that doing in the bedroom? ")
                    cnt_room = b_room
                    continue
                if bools['fed'] and not bools['spam']:
                    cnt_room = b_room
                    continue
            if inp == inputs['south']:
                print('You enter the kitchen.')
                if not bools['pantry']:
                    print('The pantry door is closed.')
                else:
                    print('The pantry door is open.')
                cnt_room = k_room
                continue
            if inp == inputs['tv'] and bools['flag_tv'] == False:
                print('You turn on the tv.')
                bools['flag_tv'] = True
                continue
            if inp == inputs['tv'] and bools['flag_tv'] == True:
                print('You turn off the tv.')
                bools['flag_tv'] = False
                continue
            if inp == inputs['feed'] and bools['bone'] and not bools['fed']:
                if bools['flag_tv'] == True:
                    print('Stella hungrily snatches the nice tasty bone out of your hand and starts to chew on it. She no longer seems to notice or care that you are here.')
                    bools['fed'] = True
                else:
                    print('Stella seems tense. She keeps glancing from the bone in your hand, to the silent tv, to you, and back to the silent tv again. Every now and then she makes a sad little noise.')
                continue
            if inp == inputs['west']:
                print('You are not ready to go outside still :(')
                continue

        if cnt_room == b_room:
            if inp == inputs['bed']:
                if bools['flag_tv']:
                    print('The noise from the tv keeps you awake. ')
                    continue
                if bools['pantry_opened'] and not bools['flag_tv']:
                    print(
                        'You keep thinking about that open pantry door and your OCD stresses you out too much to sleep.')
                    continue
                if bools['pantry'] and not bools['flag_tv']:
                    print(
                        'Wait...did you leave the pantry door unlocked? Better go check.')
                    continue
                if bools['key'] and not bools['pantry']:
                    print(
                        'The pantry in your pocket keeps digging into your leg. Best put it back.')
                    continue
                if bools['safe'] and not bools['key']:
                    print("You're pretty sure you forgot to close the safe.")
                    continue

                if bools['spam'] and not bools['pantry']:
                    print(
                        "You should really put that can of lovely spam away in the pantry first.")
                    continue
                else:
                    if bools['spam_stored']:
                        bools['asleep'] = True
            if inp == inputs['get'] and not bools['spam']:
                print("You grab the can of lovely spam.")
                bools['spam'] = True
                continue
            if inp == inputs['south']:
                living_room()
                cnt_room = l_room
                continue

        if cnt_room == o_room:
            if inp == inputs['west']:
                living_room()
                cnt_room = l_room
                continue
            if inp == inputs['get'] and bools['safe']:
                print('You remove the pantry door key from the safe.')
                bools['key'] = True
                continue
            if inp == inputs['open'] and not bools['safe']:
                print('Please enter the combination to the safe, one number at a time. You remember that it is the next three numbers in the Collatz sequence after 42')
                num1 = int(input('First number? '))
                if num1 == 21:
                    num2 = int(input('Second number? '))
                    if num2 == 64:
                        num3 = int(input('Third number? '))
                        if num3 == 32:
                            print(
                                "You hear a satisfying 'Ka-CHUNK' as the handle turns and the safe door swings invitingly open. \nInside you see the pantry door key")
                            bools['safe'] = True
                else:
                    print("Nope. that's not it. The locked safe silently mocks you.")
            if inp == inputs['put']:
                if bools['key'] and bools['safe']:
                    print('You put the pantry door key into the safe.')
                    bools['key'] = False
                    continue
            if inp == inputs['close'] and bools['safe']:
                print('You close the safe and spin the dial a few times to reset it.')
                bools['safe'] = False
                continue

        if cnt_room == k_room:
            if inp == inputs['north']:
                living_room()
                cnt_room = l_room
                continue
            if inp == inputs['unlock']:
                if not bools['key']:
                    print("The pantry door is closed. It won't open")
                else:
                    print('You unlock the pantry door.')
                    bools['pantry'] = True
                continue
            if inp == inputs['open'] and bools['pantry'] == True:
                print('The pantry door opens. \nInside you see a nice tasty bone.')
                bools['pantry_opened'] = True
                continue
            if inp == inputs['get'] and bools['pantry_opened']:
                print(
                    'You take the nice tasty bone out of the pantry. Stella watches you with great interest from the living room.')
                bools['bone'] = True
                continue
            if inp == inputs['close']:
                if bools['pantry']:
                    print('The pantry door closes.')
                    bools['pantry_opened'] = False
                continue
            if inp == inputs['lock']:
                if bools['pantry_opened'] == False and bools['key']:
                    print('You lock the pantry door.')
                    bools['pantry'] = False
            if inp == inputs['put'] and bools['pantry_opened']:
                if bools['spam']:
                    print(
                        'You put the can of lovely spam into the pantry where it belongs.')
                    bools['spam'] = False
                    bools['spam_stored'] = True
                    continue

    print('Sleep! At last! You win!')
    print(turns, 'turns played')
    return True


Project2()
