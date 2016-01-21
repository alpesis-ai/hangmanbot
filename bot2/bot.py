import settings

import hangman.hangmanserver as hangmanserver
import hangman.guessword as guessword

def main():

    print "**********************************************************"
    print "                     HANGMAN BOT                          "
    print "**********************************************************"
    print "Connecting server and login..."
    print "Connecting...\n"

    requestUrl = settings.REQUEST_URL
    playerId = settings.PLAYER_ID
    hangmanServer = hangmanserver.HangmanServer(requestUrl, playerId) 
    
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
                    letter = guessword.get_letter(word['data']['word'], guessedLetters)
                    guess = hangmanServer.guess_word(sessionId, letter.upper())
                    givenWord = guess['data']['word']
                else:
                    letter = guessword.get_letter(givenWord, guessedLetters)
                    guess = hangmanServer.guess_word(sessionId, letter.upper())
                    givenWord = guess['data']['word']
                guessedLetters.append(letter)
                guessCounter += 1
                
 
                # getresult
                result = hangmanServer.get_result(sessionId)
                incorrectWordCount = result['data']['totalWordCount'] - result['data']['correctWordCount']

                print "\nGuess: %s, guessedWord: %s, letter: %s" % (str(guessCounter), guess['data']['word'], letter)
                print "----"
                print "Score: %s" % result['data']['score']
                print "- totalWordCount: %s" % result['data']['totalWordCount']
                print "- correctWordCount: %s" % result['data']['correctWordCount']
                print "- incorrectWordCount: %s" % str(incorrectWordCount)
                print "- totalWrongGuessCount: %s" % result['data']['totalWrongGuessCount']
                print ""

                # guessIndex
                numOfUnknown = guessword.count_unknown(guess['data']['word'])                 
                if (guess['data']['wrongGuessCountOfCurrentWord'] == numberOfGuessAllowedForEachWord) \
                or (numOfUnknown == 0):
                    guessIndex = False
 
            wordCounter += 1        
 

        print "=========================================================="
        print "Session: END"
        print "=========================================================="
        # display a session score
        #if totalWordCount == numberOfWordsToGuess:
        #    score = display_result(hangmanServer, sessionId)

            # submit a session result
        #    if score >= 1100:
        #        message = hangmanbot.submit_result(hangmanServer, sessionId)
        #else:
            #score = display_result(hangmanServer, sessionId)

    else:
        raise session['message']

if __name__ == '__main__':
    main()