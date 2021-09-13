# Project by Justin Balbuena (CIIC3015-096)

import os
import time
width = os.get_terminal_size().columns

print("Welcome to JB Bank!!!\n".center(width))
time.sleep(1.5)
print('To create an account please fill out the following:\n')
time.sleep(1.2)

name = input('Enter the name for your account: ').strip()

# Error message if non int or float is entered
while True:
    try:
        balance = float(input('Enter your starting balance: '))
        break
    except:
        print(f'\nCan only deposit money to {name}, try again')

round_balance = round(balance, 2)

n_deposits, n_withdrawals, bad_withdrawals, fees = 0, 0, 0, 0
d_total, w_total, bw_total, f_total = 0, 0, 0, 0


def menu():
    global round_balance
    options = ['\nAccount name: ' + name, 'Account balance: $' + str(round_balance), 'You can: ', '1) Deposit funds into account (1/d)',
               '2) Withdraw funds from account (2/w)', '3) Quit (3/q)']
    for choices in options:
        print(choices)


def final_statement():
    global round_balance

    quit = ['\nFinal Statement:', 'Account name: ' + name, 'Account balance: $' + str(round_balance), str(n_deposits) + ' deposits totaling $' + str(d_total), str(
        n_withdrawals)+' withdrawals totaling $' + str(w_total), str(bad_withdrawals) + ' bad withdrawals totaling $' + str(bw_total), str(fees) + ' fees totaling $' + str(f_total)]
    for options in quit:
        print(options)


while(name and balance >= 0):

    menu()
    selection = input('Please enter your selection: ')
    if(selection == '1') or (selection == 'd'):
        while True:
            try:
                deposit = round(
                    float(input('Amount you wish to deposit: ')), 2)
                round_balance += deposit
                d_total += deposit
                n_deposits += 1
                break
            except:
                print('Can only deposit money!!!')

    elif(selection == '2') or (selection == 'w'):
        withdraw = round(float(input('Amount you wish to withdraw: ')), 2)
        if(withdraw <= balance):
            round_balance -= withdraw
            n_withdrawals += 1
            w_total += withdraw

        elif(withdraw > balance):
            print(
                '\nNot enough funds. A fee of $5 is being deducted from your balance. \nHave a nice day!!')
            round_balance -= 5
            fees += 1
            bad_withdrawals += 1
            bw_total += withdraw
            f_total += 5

    elif(selection == '3') or (selection == 'q'):
        final_statement()
        break
