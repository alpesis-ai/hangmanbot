import logging

import hangman.guessletter
import hangman.result

log = logging.getLogger('hangmanbot')

def start_game(hangmanServer):

    session = hangmanServer.start_game()
    log.debug("start_game: created a session, session info: %s." % session)

    if session['message'] == 'THE GAME IS ON':
        totalWordCount = process_session(hangmanServer, session)

        if (totalWordCount == session['data']['numberOfWordsToGuess']):
            message = submit_result(hangmanServer, session)
        else:
            message = session['message']
    else:
        raise session['message']

    log.debug("start_game: returns a message: %s" % message)
    return message


def process_session(hangmanServer, session):

    totalWordCount = 1
    while totalWordCount <= session['data']['numberOfWordsToGuess']:
        log.debug("totalWordCount: %s" % totalWordCount)

        word = hangmanServer.next_word(session['sessionId'])
        log.debug("word: %s" % word)
        nextIndex = _guess_word(hangmanServer, word, session['data']['numberOfGuessAllowedForEachWord'])
        if nextIndex:
            totalWordCount += 1

    return totalWordCount


def submit_result(hangmanServer, session):
   
 
    bestScore = hangman.result.get_bestscore(settings.BEST_SCORE_PATH)
    result = _get_result(hangmanServer, session['sessionId'])
    if result['data']['score'] > bestScore:
        hangman.result.save_bestscore(settings.BEST_SCORE_PATH, str(result['data']['score']))

        isSubmitText = """ \
            bestScore: {0}, thisScore: {1}.\n 
            Would you like to submit thisScore? (y/n)
        """.format(str(bestScore), str(result['data']['score']))
        isSubmit = raw_input(isSbumitText)
        if isSubmit == 'y':
            #submit = 
            print "Score submitted. Well done!"
        else:
            print "Thank you!"

    message = "GAME OVER."
    return message

#-----------------------------------------------------------------------------#


def _guess_word(hangmanServer, word, numberOfGuessAllowedForEachWord):
    
    guessedLetters = []
    guessCounter = 0
    guessIndex = True
    while guessIndex:
        
        if guessCounter == 0:
            letter = hangman.guessletter.get_letter(word['data']['word'], guessedLetters)
            guess = hangmanServer.guess_word(word['sessionId'], letter.upper())
            log.debug("guess: %s" % guess)
            givenWord = guess['data']['word']
        else:
            letter = hangman.guessletter.get_letter(givenWord, guessedLetters)
            guess = hangmanServer.guess_word(word['sessionId'], letter.upper())
            log.debug("guess: %s" % guess)
            givenWord = guess['data']['word']
        guessedLetters.append(letter)
        guessCounter += 1

        result = _get_result(hangmanServer, guess['sessionId'])
        log.debug("result: %s" % result)

        numOfUnknown = hangman.guessletter.count_unknown(guess['data']['word'])
        if (guess['data']['wrongGuessCountOfCurrentWord'] == numberOfGuessAllowedForEachWord) \
          or (numOfUnknown == 0):
            guessIndex = False


    if guessIndex is False:
        nextIndex = True

    return nextIndex

def _get_result(hangmanServer, sessionId):

    result = hangmanServer.get_result(sessionId)
    return result
