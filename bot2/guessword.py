import time
from collections import deque

import settings
import dictionary
import patterns

#--------------------------------------------------------------------------#
# 1. filling in the vowels
# 2. checking against the words from a dictionary

#WORDDICT = dictionary.split_dict()

def guess_word(client, sessionId, wordLength, unknownLetters):

    counter = 0

    correctLetters = []
    incorrectLetters = []

    dictBook = deque(settings.OPTIMIZED_DICT_BOOK[wordLength])
    while unknownLetters == wordLength:
        time.sleep(1)        
        counter += 1
        print "---------------------------------------------------"
        print "Optimized Dict Book"
        print "---------------------------------------------------"
        print "ROUND: %s" % counter

 
        letter = dictBook.popleft()
        guess = client.guess_word(sessionId, letter.upper())
        unknownLetters = patterns.unknown_letters(guess['data']['word'])
        if unknownLetters == wordLength:
            incorrectLetters.append(letter.lower())
        else:
            correctLetters.append(letter.lower())

        print "GUESS: %s" % guess
        print "WORD: %s" % guess['data']['word']
        print "incorrectLetters: %s" % incorrectLetters
        print "correctLetters: %s" % correctLetters

    while unknownLetters > 0:

        guessedLetters = correctLetters + incorrectLetters
        pattern = patterns.create_pattern(guess['data']['word'], guessedLetters)
        matches = dictionary.search_pattern(settings.WORDDICT, guess['data']['word'], pattern)

        if len(matches) > 0:
            matches = deque(matches)
            print "matches: %s" % matches

            match = matches.popleft()
            for letter in match:
                if (letter not in incorrectLetters) and (letter not in correctLetters):
                    guess = client.guess_word(sessionId, letter.upper())
                    if guess['data']['wrongGuessCountOfCurrentWord'] < 10:
                        preUnknownLetters = unknownLetters
                        unknownLetters = patterns.unknown_letters(guess['data']['word'])
                        if unknownLetters == preUnknownLetters:
                            incorrectLetters.append(letter)
                            
                            time.sleep(1)        
                            counter += 1
                            print "---------------------------------------------------"
                            print "Search Pattern: Wrong"
                            print "---------------------------------------------------"
                            print "ROUND: %s" % counter
                            print "GUESS: %s" % guess
                            print "WORD: %s" % guess['data']['word']
                            print "letter: %s" % letter
                            print "incorrectLetters: %s" % incorrectLetters
                            print "correctLetters: %s" % correctLetters
                            print "WRONG!"
                            break

                        elif unknownLetters == 0:
                            time.sleep(1)        
                            counter += 1
                            print "---------------------------------------------------"
                            print "Search Pattern: Correct && End"
                            print "---------------------------------------------------"
                            print "ROUND: %s" % counter
                            print "GUESS: %s" % guess
                            print "WORD: %s" % guess['data']['word']
                            print "letter: %s" % letter
                            print "incorrectLetters: %s" % incorrectLetters
                            print "correctLetters: %s" % correctLetters
                            print "END"
                            return unknownLetters, guess['data']['word']

                        elif unknownLetters < preUnknownLetters:
                            correctLetters.append(letter)

                            time.sleep(1)        
                            counter += 1
                            print "---------------------------------------------------"
                            print "Search Pattern: Correct"
                            print "---------------------------------------------------"
                            print "ROUND: %s" % counter
                            print "GUESS: %s" % guess
                            print "WORD: %s" % guess['data']['word']
                            print "letter: %s" % letter
                            print "incorrectLetters: %s" % incorrectLetters
                            print "correctLetters: %s" % correctLetters
                            print "CORRECT"
                            break
                        else:
                            break
                    else:
                        time.sleep(1)        
                        counter += 1
                        print "---------------------------------------------------"
                        print "Search Pattern: Wrong && End"
                        print "---------------------------------------------------"
                        print "ROUND: %s" % counter

                        # if guess > 10, make unknownLetters = 0 to stop the loop
                        # return the value to stop the guess
                        unknownLetters = 0
                        return unknownLetters, guess['data']['word']
        else:
            nonGuessedLetters = [letter for letter in settings.ALPHABET if letter not in guessedLetters]
            for letter in nonGuessedLetters:
                guess = client.guess_word(sessionId, letter.upper()) 
                if guess['data']['wrongGuessCountOfCurrentWord'] < 10:
                    preUnknownLetters = unknownLetters
                    unknownLetters = patterns.unknown_letters(guess['data']['word'])
                    if unknownLetters == preUnknownLetters:
                        incorrectLetters.append(letter.lower())

                        time.sleep(1)        
                        counter += 1
                        print "---------------------------------------------------"
                        print "Search Alphabet: Wrong"
                        print "---------------------------------------------------"
                        print "ROUND: %s" % counter
                        print "GUESS: %s" % guess
                        print "WORD: %s" % guess['data']['word']
                        print "letter: %s" % letter
                        print "incorrectLetters: %s" % incorrectLetters
                        print "correctLetters: %s" % correctLetters
                        print "WRONG!"
                        break

                    elif unknownLetters == 0:
                        time.sleep(1)        
                        counter += 1
                        print "---------------------------------------------------"
                        print "Search Alphabet: Correct && End"
                        print "---------------------------------------------------"
                        print "ROUND: %s" % counter
                        print "GUESS: %s" % guess
                        print "WORD: %s" % guess['data']['word']
                        print "letter: %s" % letter
                        print "incorrectLetters: %s" % incorrectLetters
                        print "correctLetters: %s" % correctLetters
                        print "END"
                        return unknownLetters, guess['data']['word']

                    elif unknownLetters < preUnknownLetters:
                        correctLetters.append(letter.lower())

                        time.sleep(1)        
                        counter += 1
                        print "---------------------------------------------------"
                        print "Search Alphabet: Correct"
                        print "---------------------------------------------------"
                        print "ROUND: %s" % counter
                        print "GUESS: %s" % guess
                        print "WORD: %s" % guess['data']['word']
                        print "letter: %s" % letter
                        print "incorrectLetters: %s" % incorrectLetters
                        print "correctLetters: %s" % correctLetters
                        print "CORRECT"
                        break
                    else:
                        break
                else:
                    time.sleep(1)        
                    counter += 1
                    print "---------------------------------------------------"
                    print "Search Alphabet: Wrong && End"
                    print "---------------------------------------------------"
                    print "ROUND: %s" % counter

                    # if guess > 10, make unknownLetters = 0 to stop the loop
                    # return the value to stop the guess
                    unknownLetters = 0
                    return unknownLetters, guess['data']['word']
