######################################
Design
######################################

*********************
Hangman Game
*********************

1. Start Game
2. Give Me A Word
3. Make A Guess
4. Get Your Result
5. Submit Your Result

------------------
Hangman Server
------------------

1. Start Game

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"playerId":"kwailamchan@hotmail.com", "action":"startGame"}'

    {"message":"THE GAME IS ON","sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a","data":{"numberOfWordsToGuess":80,"numberOfGuessAllowedForEachWord":10}}


2. Give Me A Word

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a", "action":"nextWord"}'

    {"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a","data":{"word":"*****","totalWordCount":1,"wrongGuessCountOfCurrentWord":0}}


3. Make A Guess

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a", "action":"guessWord", "guess" : "P"}'

    {"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a","data":{"word":"*****","totalWordCount":1,"wrongGuessCountOfCurrentWord":1}}


4. Get Your Result

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a", "action":"getResult"}'

    {"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a","data":{"totalWordCount":0,"correctWordCount":0,"totalWrongGuessCount":0,"score":0}}


5. Submit Your Result

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json    " --data '{"sessionId":"e6a7d693a9dbd53eb11d08d8743b7642", "action":"submitResult"}'

    {"message":"GAME OVER","sessionId":"e6a7d693a9dbd53eb11d08d8743b7642","data":{"playerId":"kwailamchan@hotmail.com","sessionId":"e6a7d693a9dbd53eb11d08d8743b7642","totalWordCount":80,"correctWordCount":70,"totalWrongGuessCount":318,"score":1082,"datetime":"2016-01-21 18:09:47"}}


    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"sessionId":"170f1f8c06b0f0fe039e0e0810436c18", "action":"submitResult"}'

    {"message":"GAME OVER","sessionId":"170f1f8c06b0f0fe039e0e0810436c18","data":{"playerId":"kwailamchan@hotmail.com","sessionId":"170f1f8c06b0f0fe039e0e0810436c18","totalWordCount":80,"correctWordCount":77,"totalWrongGuessCount":269,"score":1271,"datetime":"2016-01-22 08:26:29"}}


    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"sessionId":"2ad8f8430e3681c4dea8696ae19fb323", "action":"submitResult"}'

    {"message":"GAME OVER","sessionId":"2ad8f8430e3681c4dea8696ae19fb323","data":{"playerId":"kwailamchan@hotmail.com","sessionId":"2ad8f8430e3681c4dea8696ae19fb323","totalWordCount":80,"correctWordCount":78,"totalWrongGuessCount":231,"score":1329,"datetime":"2016-01-22 14:26:57"}}

*********************
HangmanBot Strategy
*********************

From the game flow, we can find the game patterns:

Score Calculation

::

    scoreOfEachWord = 20 - incorrectGuessCount

If you want to get a higher score, it means you must improve the correctness of each guess.
The correctness of each guess is the letter, this letter is in a word, then we can try to
figure out the letter patterns in the words.

--------------------------
English Word Elements
--------------------------

Rules:

- Each Word (most of the words) = prefix + word root + sufix.
- Word Root = vowel + consonant

-----------------------------
Strategy of Letter Selection
-----------------------------

Steps:

1. find a dictionary
2. count the unknown letters of a given word
3. (guess) fill in a vowel
4. (guess) search the word pattern in a dictionary, get matchedWords
5. (guess) search the letter patterns in a word, select a letter (excluded guessedLetters) 


::

       get_letter()
            |
            |---> count_unknown()
            |
            |---> _search_vowels()
            |---> _search_pattern()
                      |
                      |---> _create_word_pattern()
                      |---> _search_word_pattern()
                      |
                      |---> _create_letter_pattern() --> _find_ngram()
                      |---> _match_letter_pattern()
                      |---> _select_letter()


**********************
HangmanBot Features
**********************

Three Models:

- HangmanServer
- HangmanBot
- Score

Additional Features:

- Logging

Features Pending:

- Analyzer
