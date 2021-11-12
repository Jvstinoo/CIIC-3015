def changey(dic, name, year):
    if name in dic:
        dic[name] = year
        print(dic)
    else:
        print('That name is not found.')
