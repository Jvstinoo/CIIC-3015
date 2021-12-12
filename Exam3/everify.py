'''Write a function called everify() which takes a dictionary and a filename as its arguments.  The dictionary contains usernames as the 
keys and 
passwords as the values. Each line of the file contains a username and its corresponding password separated by a colon :

The function will check every username and password in the dictionary against the values in the password file. If the password in the 
dictionary does not match
the password in the file, update the dictionary with the password from the file. If the passwords match, or if the username does not exist 
in the password file, then 
do not change the dictionary for that username.

The function returns the updated dictionary.

Hint: You can use your solution from the previous problem as a helper function in this problem.'''


def everify(dic, f):
    fopen = open(f)
    for line in fopen:
        colon = line.find(':')
        colonStrip = line.strip().split(':')
        if colonStrip[0] in dic:
            if dic[colonStrip[0]] != colonStrip[1]:
                dic[colonStrip[0]] = line[colon+1:].strip()
    fopen.close()
    return dic


D = {"sofia": "atari", "nestor": "sweetroll", "javier": "Angelo"}
print(everify(D, "pass0.txt"))
