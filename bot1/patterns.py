def unknown_letters(guessWord):
    counter = 0
    for letter in guessWord:
        if letter == '*':
            counter += 1
    return counter

def create_pattern(guessWord, guessedLetters):

    # pattern: [^iac][^iac]ia[^iac]
    letters = [letter.lower() for letter in guessedLetters]
    subPattern = '[^' + ''.join(letter for letter in letters) + ']'
    pattern = [subPattern if letter == '*' else letter.lower() for letter in guessWord]
    pattern = ''.join(letter for letter in pattern)
    print "pattern: %s " % pattern

    return pattern
    
