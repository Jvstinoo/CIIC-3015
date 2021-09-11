'''You are playing a game of rock/paper/scissors with a friend. The rules are:

    'rock' beats 'scissors'
    'scissors' beats 'paper'
    'paper' beats 'rock'

However, you have both had quite a lot to drink, so there is a great deal of noise in your input strings. You cannot assume that all characters are lowercase. Worse, there may be garbage characters in the input strings before and/or after the actual move. (Hint: You can use the find() string method here, the details of which can be found at python.org.) You may assume that every input string does contain exactly one valid move somewhere inside it.

Write a function called DoIWin() which takes two string parameters. The first string is your move, the second string is your friend's move. Return True if and only if you win that round - if you lose, or if the round is tied, return False.

'''


def DoIWin(move1, move2):
    move1, move2 = move1.lower(), move2.lower()

    if(move1.find('rock') != -1 and move2.find('isso') != -1):
        return True
    elif(move1.find('isso') != -1 and move2.find('paper') != -1):
        return True
    elif(move1.find('paper') != -1 and move2.find('rock') != -1):
        return True
    return False


print(DoIWin('crock', 'paper'))


print(DoIWin('rock', 'scissors'))
