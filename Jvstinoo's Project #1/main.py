'''Ideas to optimize project: 

strip the inputs
lowercase/uppercase
if input is only number, dont throw error just repeat the process or show message saying:
    Input needs to be a number.
    Something like that

'''
import os
import time
width = os.get_terminal_size().columns

print("Welcome to JB Bank!!!\n".center(width))
time.sleep(1.5)
print('To create an account please fill out the following:\n')
time.sleep(0.8)


name = input('Enter the name for your account: ')
balance = float(input('Enter your starting balance: '))

# Counter to keep track of the deposits and withdrawals
n_deposits, n_withdrawals, bad_withdrawals, fees = 0, 0, 0, 0

# Counter to keep track of the amount of transactions of each
d_total, w_total, bw_total, f_total = 0, 0, 0, 0

# Menu in array so I dont have to repeat, just loop through it


def menu():
    global balance
    options = ['\nAccount name: ' + name, 'Account balance: $' + str(balance), 'You may: ', '1) Deposit funds into account (1/d)',
               '2) Withdraw funds from account (2/w)', '3) Quit. (3/q)']
    for choices in options:
        print(choices)

# Final statement in array so I can loop through it


def final_statement():
    global balance
    quit = ['\nFinal Statement:', 'Account name: ' + name, 'Account balance: $' + str(balance), str(n_deposits) + ' deposits totaling $' + str(d_total), str(
        n_withdrawals)+' withdrawals totaling $' + str(w_total), str(bad_withdrawals) + ' bad withdrawals totaling $' + str(bw_total), str(fees) + ' fees totaling $' + str(f_total)]
    for options in quit:
        print(options)


# Main loop
while(name and balance):
    menu()
    selection = input('Please enter your selection: ')
    if(selection == '1'):
        deposit = float(input('Amount you wish to deposit: '))
        balance += deposit
        d_total += deposit
        n_deposits += 1

    elif(selection == '2'):
        withdraw = float(input('Amount you wish to withdraw: '))
        if(withdraw > balance):
            print('\nInsufficient funds. An overdraft fee of $5 is being deducted from your balance. \nHave a nice day!!')
            balance -= 5
            fees += 1
            bad_withdrawals += 1
            bw_total += withdraw
            f_total += 5

        elif(withdraw <= balance):
            balance -= withdraw
            n_withdrawals += 1
            w_total += withdraw

    elif(selection == '3'):
        final_statement()
        break
