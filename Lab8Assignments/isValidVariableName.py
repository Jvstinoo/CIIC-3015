def IsValidVariableName(s):

    for i in s:
        if i.isdigit() or i.isspace():
            return False
    if not s:
        return False

    return True
