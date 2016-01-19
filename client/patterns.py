def unknown_letters(guessWord):
    counter = 0
    for letter in guessWord:
        if letter == '*':
            counter += 1
    return counter
