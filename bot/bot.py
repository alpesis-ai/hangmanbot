import settings

import hangman.hangmanserver
import hangman.guessletter
import hangman.result

import dicts.wordcollector

def main():

    print "**********************************************************"
    print "                     HANGMAN BOT                          "
    print "**********************************************************"
    print "Connecting server and login..."
    print "Connecting...\n"

    requestUrl = settings.REQUEST_URL
    playerId = settings.PLAYER_ID
    hangmanServer = hangman.hangmanserver.HangmanServer(requestUrl, playerId) 
    
    print "Now you are onboard."
    print "Welcome, %s." % playerId
    print ""
    print "Starting a game..."

    session = hangmanServer.start_game()
    if session['message'] == 'THE GAME IS ON':

        print "Game started."
        print "=========================================================="
        print "Session: START"
        print "=========================================================="

        # start a session
        sessionId = session['sessionId']
        numberOfWordsToGuess = session['data']['numberOfWordsToGuess']
        numberOfGuessAllowedForEachWord = session['data']['numberOfGuessAllowedForEachWord']
        print "Session Info:\n"
        print "- sessionId: %s" % sessionId
        print "- numberOfWordsToGuess: %s" % numberOfWordsToGuess
        print "- numberOfGuessAllowedForEachWord: %s" % numberOfGuessAllowedForEachWord


        print "=========================================================="
        print "Session: ON"
        print "=========================================================="
        print "Getting a new word..."
        # play a session: nextword + guessword + getresult
        
        # nextword 
        wordCounter = 1
        while wordCounter <= numberOfWordsToGuess:
              
            # nextword
            word = hangmanServer.next_word(sessionId)

            print "----------------------------------------------------------"
            print "sessionId: %s" % sessionId
            print "wordCounter: %s" % wordCounter
            print "givenWord: %s" % word['data']['word']
            print "----------------------------------------------------------"
            

            # guessword + getresult
            guessedLetters = []
            guessCounter = 0
            guessIndex = True
            while guessIndex:

                # guessword
                if guessCounter == 0:
                    letter = hangman.guessletter.get_letter(word['data']['word'], guessedLetters)
                    guess = hangmanServer.guess_word(sessionId, letter.upper())
                    givenWord = guess['data']['word']
                else:
                    letter = hangman.guessletter.get_letter(givenWord, guessedLetters)
                    guess = hangmanServer.guess_word(sessionId, letter.upper())
                    givenWord = guess['data']['word']
                guessedLetters.append(letter)
                guessCounter += 1
                
 
                # getresult
                result = hangmanServer.get_result(sessionId)
                incorrectWordCount = result['data']['totalWordCount'] - result['data']['correctWordCount']

                print "----------------------------------------------------------"
                print "sessionId: %s" % sessionId
                print "wordCounter: %s, Guess: %s, guessedWord: %s" % (wordCounter, str(guessCounter), guess['data']['word'])
                print "----------------------------------------------------------"
                print "- letter: %s" % letter
                print "- guessedLetters: %s" % guessedLetters
                print "- wrongGuessCountOfCurrentWord: %s" % guess['data']['wrongGuessCountOfCurrentWord']
                print ""
                print "Score: %s" % result['data']['score']
                print "- totalWordCount: %s" % result['data']['totalWordCount']
                print "- correctWordCount: %s" % result['data']['correctWordCount']
                print "- incorrectWordCount: %s" % str(incorrectWordCount)
                print "- totalWrongGuessCount: %s" % result['data']['totalWrongGuessCount']
                print "----------------------------------------------------------"

                # guessIndex
                numOfUnknown = hangman.guessletter.count_unknown(guess['data']['word'])                 
                if (guess['data']['wrongGuessCountOfCurrentWord'] == numberOfGuessAllowedForEachWord) \
                or (numOfUnknown == 0):
                    dicts.wordcollector.collect_words(guess['data']['word'])
                    guessIndex = False
 
            wordCounter += 1        
 

        print "=========================================================="
        print "Session: END"
        print "=========================================================="

        # score board
        bestScore = hangman.result.get_bestscore(settings.BEST_SCORE_PATH)
        
        print "----------------------------------------------------------"
        print "Score Board: (best score: %s)" % str(bestScore)
        print "----------------------------------------------------------"
        print ""
        print "sessionScore: %s" % result['data']['score']
        print "- totalWordCount: %s" % result['data']['totalWordCount']
        print "- correctWordCount: %s" % result['data']['correctWordCount']
        print "- incorrectWordCount: %s" % str(incorrectWordCount)
        print "- totalWrongGuessCount: %s" % result['data']['totalWrongGuessCount'] 
        print "----------------------------------------------------------"

        if (result['data']['totalWordCount'] == numberOfWordsToGuess) and \
           (result['data']['score'] > bestScore):
            hangman.result.save_bestscore(settings.BEST_SCORE_PATH, str(result['data']['score'])) 
            isSubmit = raw_input("Would you like to submit this score? (y/n)")
            if isSubmit == 'y':
                print "Score submitted. Well done!"
            else:
                print "Thank you!"

    else:
        raise session['message']

if __name__ == '__main__':
    main()
