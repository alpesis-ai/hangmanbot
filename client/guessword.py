from collections import deque

import dictionary
import patterns

VOWELS = deque(['o', 'a', 'i', 'e', 'u'])
WORDDICT = dictionary.split_dict()

def guess_word(client, sessionId, wordLength, unknownLetters):

    correctLetters = []
    incorrectLetters = []


    while unknownLetters == wordLength:
        vowel = VOWELS.popleft()
        guess = client.guess_word(sessionId, vowel.upper())
        unknownLetters = patterns.unknown_letters(guess['data']['word'])
        if unknownLetters == wordLength:
            incorrectLetters.append(vowel)
        else:
            correctLetters.append(vowel)

        print "================================================="
        print "GUESS: %s" % guess
        print "incorrectLetters: %s" % incorrectLetters
        print "correctLetters: %s" % correctLetters


    while unknownLetters > 0:

        matches = dictionary.search_pattern(WORDDICT, guess['data']['word'])
        if len(incorrectLetters) > 0:
            for letter in incorrectLetters:
                for match in matches:
                    if letter in match:
                        matches.remove(match)

        matches = deque(matches)
        match = matches.popleft()
        for letter in match:
            print "match: %s" % match
            if letter not in incorrectLetters and letter not in correctLetters:
                guess = client.guess_word(sessionId, letter.upper())
                preUnknownLetters = unknownLetters
                unknownLetters = patterns.unknown_letters(guess['data']['word'])
                if unknownLetters == preUnknownLetters:
                    incorrectLetters.append(letter)
                    print "================================================="
                    print "GUESS: %s" % guess
                    print "letter: %s" % letter
                    print "incorrectLetters: %s" % incorrectLetters
                    print "correctLetters: %s" % correctLetters
                    print "preUnknownLetters: %s" % preUnknownLetters
                    print "unknownLetters: %s" % unknownLetters
                    continue
                else:
                    correctLetters.append(letter)
                    print "================================================="
                    print "GUESS: %s" % guess
                    print "letter: %s" % letter
                    print "incorrectLetters: %s" % incorrectLetters
                    print "correctLetters: %s" % correctLetters
                    print "preUnknownLetters: %s" % preUnknownLetters
                    print "unknownLetters: %s" % unknownLetters

    return unknownLetters
