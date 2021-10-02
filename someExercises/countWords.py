def count_words(str):
    counter = 1

    for i in str[:]:
        if(i == ' '):
            counter += 1
    return counter


print(count_words("What is your name?"))
