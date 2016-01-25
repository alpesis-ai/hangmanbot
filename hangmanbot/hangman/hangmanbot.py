"""
HangmanBot
===============================================================================
---------------
Game Process
---------------
                      <LOOP>        <LOOP>
    session starts -> get a word -> guess a letter  -> submit result -> END
                                 -> get this result
---------------
Methods
---------------
    start_game()
        |
        |---> SESSION
        |---> process_session()
        |          |---- WORD
        |          |---> _guess_word()
        |                     |---> letter=hangman.guessletter.get_letter()
        |                     |---> GUESS
        |                     |---> _get_result()
        |                               |---> RESULT
        |
        |---> process_result()
                   |---> _update_best_score()
                   |          |---> _get_result()
                   |                    |---> RESULT
                   |---> _submit_score()
                              |---> SUBMIT
  NOTE:
  * hangman.guessletter.get_letter(): returns a letter that matching the word
"""

import logging

import settings.settings as settings

import dicts.wordcollector

import hangman.guessletter
import hangman.result

LOG = logging.getLogger('hangmanbot')


def start_game(hangmanServer):
    """(startGame)
    Starting the game and creating a session.
    """

    session = hangmanServer.start_game()
    LOG.info("session: %s." % session)

    if session['message'] == 'THE GAME IS ON':
        totalWordCount = process_session(hangmanServer, session)

        if totalWordCount == session['data']['numberOfWordsToGuess']:
            message = process_result(hangmanServer, session)
        else:
            message = session['message']
    else:
        raise session['message']
        LOG.error("SessionError: message: %s" % message)

    LOG.info("message: %s" % message)
    return message


def process_session(hangmanServer, session):
    """(nextWord)
    Getting the words and call the guess process.
    """

    totalWordCount = 1
    while totalWordCount <= session['data']['numberOfWordsToGuess']:
        LOG.debug("totalWordCount: %s" % totalWordCount)

        word = hangmanServer.next_word(session['sessionId'])
        LOG.info("word: %s" % word)
        numOfGuessAllowed = session['data']['numberOfGuessAllowedForEachWord']
        nextIndex = _guess_word(hangmanServer, word, numOfGuessAllowed)
        if nextIndex:
            totalWordCount += 1

    return totalWordCount


def process_result(hangmanServer, session):
    """(getResult/submitResult)
    Getting the session result and submitting the score.
    """

    bestScore, thisScore = _update_best_score(hangmanServer, session)
    message = _submit_result(hangmanServer, session, bestScore, thisScore)

    return message

#-----------------------------------------------------------------------------#


def _guess_word(hangmanServer, word, numberOfGuessAllowedForEachWord):
    """(guessWord)
    Guessing the letters of a word and displaying the result of each guess.
    """

    guessCounter = 0
    guessedLetters = []

    guessIndex = True
    while guessIndex:

        if guessCounter == 0:
            givenWord = word['data']['word']
            letter = hangman.guessletter.get_letter(givenWord, guessedLetters)
            guess = hangmanServer.guess_word(word['sessionId'], letter.upper())
            givenWord = guess['data']['word']
        else:
            letter = hangman.guessletter.get_letter(givenWord, guessedLetters)
            guess = hangmanServer.guess_word(word['sessionId'], letter.upper())
            givenWord = guess['data']['word']
        guessedLetters.append(letter)
        LOG.debug("letter: %s" % letter)
        LOG.debug("guess: %s" % guess)
        LOG.debug("givenWord: %s" % givenWord)
        LOG.info("guessCounter: %s" % guessCounter)
        guessCounter += 1

        result = _get_result(hangmanServer, guess['sessionId'])
        LOG.info("result: %s" % result)

        numOfUnknown = hangman.guessletter.count_unknown(guess['data']['word'])
        wrongGuessCount = guess['data']['wrongGuessCountOfCurrentWord']
        if (wrongGuessCount == numberOfGuessAllowedForEachWord) or \
           (numOfUnknown == 0):
            dicts.wordcollector.collect_words(guess['data']['word'])
            LOG.info("guessedWord: %s" % guess['data']['word'])
            guessIndex = False

    if guessIndex is False:
        nextIndex = True
    return nextIndex


def _update_best_score(hangmanServer, session):
    """Updating the bestScore if thisScore > lastBestScore.
    """

    result = _get_result(hangmanServer, session['sessionId'])
    thisScore = result['data']['score']

    bestScore = hangman.result.get_bestscore(settings.BEST_SCORE_PATH)
    if thisScore > bestScore:
        hangman.result.save_bestscore(settings.BEST_SCORE_PATH,
                                      str(result['data']['score']))
    return bestScore, thisScore


def _submit_result(hangmanServer, session, bestScore, thisScore):
    """(submitResult)
    Submitting the Result if a user agrees.
    """

    isSubmitText = """
        bestScore: {0}, thisScore: {1}.\n
        Would you like to submit thisScore? (y/n)
    """.format(str(bestScore), str(thisScore))

    isSubmit = raw_input(isSubmitText)
    if isSubmit == 'y':
        #submit =
        print "Score submitted. Well done!"
    else:
        print "Thank you!"

    message = "GAME OVER."
    return message


def _get_result(hangmanServer, sessionId):
    """(getResult) Getting the result.
    """

    result = hangmanServer.get_result(sessionId)
    return result
