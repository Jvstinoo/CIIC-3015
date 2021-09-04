'''Project Breakout:
First, ask user for account name and balance.
Enter main loop, show name, balance and a few options:
1) Deposit some funds,
2) Withdraw some funds,
3) Quit.

For option 1 and 2, ask user for amount they want to deposit or withdraw.

For now, I'll start by doing these.

options = {'1) Deposit funds into account': '1', '2) Withdraw funds from account': '2', '3) Quit.':'3'}

Idea: Do three loops, for each of the options and just run through them depending on the choice of user...

Strip input or lowercase, uppercase; all things like that. If not number, repeat shit like that

if(selection == '2'):
        withdraw = float(input('Amount you wish to withdraw: '))
        if(withdraw > balance):
            print('Insufficient funds. For your convenience, an overdraft fee of $5 is being deducted from your balance. Have a nice day!!')
            balance -= 5
            print(nums)
        selection = input('Please enter your selection: ')
'''
name = input('Please enter the name for your account: ')
balance = float(input('Please enter your starting balance: '))

n_deposits = 0
n_withdrawals = 0
bad_withdrawals = 0
fees = 0

d_total = 0
w_total = 0
bw_total = 0
f_total = 0


def menu():
    global balance
    options = ['Account name: ' + name, 'Account balance: $' + str(balance), 'You may: ', '1) Deposit funds into account',
               '2) Withdraw funds from account', '3) Quit.']
    for choices in options:
        print(choices)


def final_statement():
    global balance
    quit = ['Final Statement', 'Account name: ' + name, 'Account balance: $' + str(balance), str(n_deposits) + ' deposits totaling $' + str(d_total), str(
        n_withdrawals)+' withdrawals totaling $' + str(w_total), str(bad_withdrawals) + ' bad withdrawals totaling $' + str(bw_total), str(fees) + ' fees totaling $' + str(f_total)]
    for options in quit:
        print(options)


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
            print('Insufficient funds. An overdraft fee of $5 is being deducted from your balance. \nHave a nice day!!')
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
