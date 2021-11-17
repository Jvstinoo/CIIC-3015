'''Write a function called userpass() which takes three string arguments: an username, a password, and a filename.
Each line of the file contains a username and its password separated by a colon :
The function will verify whether the username exists in the file and whether the password is the correct one.

The function will return a tuple for each of the following cases:

1.     If the username is found and the password is correct: 

        The function will return the tuple:(True, line) where line is the stripped line in the password file which matches the username

2.     If the username is found and the password is incorrect: 

        The function will return the tuple: (False, line) where line is the stripped line in the password file which matches the username

3.     If the username is not found:

        The function will return the tuple:(False, None)'''


def userpass(user, passw, f):
    fopen = open(f)
    for line in fopen:
        if user in line:
            if passw in line:
                return (True, line.strip())
            else:
                return (False, line.strip())
    return (False, None)

    fopen.close()


'''def userpass(username, password, filename):
    fopen = open(filename)
    for line in fopen:
        if username in line:
            if password in line.strip():
                return (True, line)
            else:
                return (False, line)
        else:
            return (False, None)
    fopen.close()


print(userpass("eric", "spam spam spam", "pass0.txt"))
'''
