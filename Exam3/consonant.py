def LastConsonant(s):
    if len(s) == 0:
        return None
    if s[-1].lower() in 'bcdfghjklmnpqrstvwxyz':
        return s[-1]
    else:
        return LastConsonant(s[:-1])


print(LastConsonant('spasmo'))
print(LastConsonant('!@#$%^&*()Z_:; <>a{}[]'))
