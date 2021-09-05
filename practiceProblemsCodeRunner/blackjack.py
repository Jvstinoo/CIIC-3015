card1 = input('Enter card #1: ')
card2 = input('Enter card #2: ')

cards = ['K', 'J', 'Q', '10']

blackjack = False

if(card1 and card2):
    for card in cards:
        if(card1 == card) and (card2 == 'A') or (card1 == 'A') and (card2 == card):
            print('Blackjack')
            blackjack = True

if not blackjack:
    print('Regular hand')
