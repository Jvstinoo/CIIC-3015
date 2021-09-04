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
'''

name = input('Please enter the name for your account: ')
balance = float(input('Please enter your starting balance: '))

options = ['Account name: ' + name, 'Account balance: ' + str(balance), 'You may: ', '1) Deposit funds into account',
           '2) Withdraw funds from account', '3) Quit.']

if(name and balance):
    for nums in options:
        print(nums)
    selection = input('Please enter your selection: ')
    if(selection == '1'):
        deposit = float(input('Amount you wish to deposit: '))
        balance += deposit
        print('$', balance)
    print(nums)
    if(selection == '2'):
        withdraw = float(input('Amount you wish to withdraw: '))
        if(withdraw > balance):
            print('Insufficient funds. For your convenience, an overdraft fee of $5 is being deducted from your balance. Have a nice day!!')
            balance -= 5
            print(nums)
        selection = input('Please enter your selection: ')
