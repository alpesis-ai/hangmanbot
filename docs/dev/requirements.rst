Requirements
==========================================

Steps:

1. Start Game
2. Give Me A Word
3. Make A Guess
4. Get Your Result
5. Submit Your Result

- New Word(step2)
  - wooly, 
- Guess (step3)
  - firstly, aeiou (o
  - secondly, fnlymn...
  - dictionary -> len(word) -> len(words) in dict -> split freq(aeiouxd) -> fill (aeiou) -> search (selected words) -> fill others
  - count the length of the word
  - log which letters have been guessed
  - if the word is correct, should not guess any more, otherwise, it will count it as wrong
    the score will be -1, total score -1. (if correct, stop)
  - if > 10, no more guess left, don't -1
- Scores (step4): show it all the time, wrong guess -1, correct +20, score = correct - wrong


::

    # http://www-01.sil.org/linguistics/wordlists/english/
    $ wget http://www.math.sjsu.edu/~foster/dictionary.txt

sessionIds:
- manual: a1662beedb0b4d1ab9ae476b73b1af2a
- dev: 9971fd554c52f23c5392544341a57766
- dev: daaa127111bd43210e56f2a008293d04
- dev: 29d5e6918ea4a43385f5f40496fb1f2f
- dev: 649931d9a0e6449c60942043a441a9d0
- dev: 1d3b5d845c84e6cb1d792baedf50f98a
- dev: 1a0d8e4f689e6341e6656b3736026d3c


errors:
- start game
  - {"message":"Problems parsing JSON"}
  - "message":"THE GAME IS ON"
  - sessionId":"9971fd554c52f23c5392544341a57766"
  - 
- Guess
  - vowels -> correct words -> dictionary -> alphabet
  - {u'message': u'You are not following the game flow'}

>>> ''.join('*' for x in range(20) if x < 20)
'********************'

- Request URL: https://strikingly-hangman.herokuapp.com/game/on
- Player ID: kwailamchan@hotmail.com

**a**
[*a]
[a*]

**ab*
[*ab]
[ab*]

a(*)b

*abc*
[*abc]
[abc*]


1. Start Game
-------------------------------------

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"playerId":"kwailamchan@hotmail.com", "action":"startGame"}'

    {"message":"THE GAME IS ON","sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a","data":{"numberOfWordsToGuess":80,"numberOfGuessAllowedForEachWord":10}}


2. Give Me A Word
-------------------------------------

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a", "action":"nextWord"}'

    {"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a","data":{"word":"*****","totalWordCount":1,"wrongGuessCountOfCurrentWord":0}}

3. Make A Guess
-------------------------------------

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a", "action":"guessWord", "guess" : "P"}'

    $ {"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a","data":{"word":"*****","totalWordCount":1,"wrongGuessCountOfCurrentWord":1}}


4. Get Your Result
-------------------------------------

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json" --data '{"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a", "action":"getResult"}'

    {"sessionId":"a1662beedb0b4d1ab9ae476b73b1af2a","data":{"totalWordCount":0,"correctWordCount":0,"totalWrongGuessCount":0,"score":0}}


5. Submit Your Result
-------------------------------------

::

    $ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/json    " --data '{"sessionId":"e6a7d693a9dbd53eb11d08d8743b7642", "action":"submitResult"}'

    {"message":"GAME OVER","sessionId":"e6a7d693a9dbd53eb11d08d8743b7642","data":{"playerId":"kwailamchan@hotmail.com","sessionId":"e6a7d693a9dbd53eb11d08d8743b7642","totalWordCount":80,"correctWordCount":70,"totalWrongGuessCount":318,"score":1082,"datetime":"2016-01-21 18:09:47"}}(hangman_client)hangman@vagrant-ubuntu-trusty-64:/hangman/hangman_client/hangman_client/client$


    (hangman_client)hangman@vagrant-ubuntu-trusty-64:/hangman/hangman_client/hangman_client/bot2$ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/jso    n    " --data '{"sessionId":"170f1f8c06b0f0fe039e0e0810436c18", "action":"submitResult"}'

    {"message":"GAME OVER","sessionId":"170f1f8c06b0f0fe039e0e0810436c18","data":{"playerId":"kwailamchan@hotmail.com","sessionId":"170f1f8c06b0f0fe039e0e0810436c18","totalWordCount":80,"correctWordCount":77,"totalWrongGuessCount":269,"score":1271,"datetime":"2016-01-22 08:26:29"}}(hangman_client)hangman@vagrant-ubuntu-trusty-64:/hangman/hangman_client/hangman_client/bot2$


    (hangman_client)hangman@vagrant-ubuntu-trusty-64:/hangman/hangman_client/hangman_client/bot2$ curl -X POST https://strikingly-hangman.herokuapp.com/game/on -H "Content-Type:application/jso    n    " --data '{"sessionId":"2ad8f8430e3681c4dea8696ae19fb323", "action":"submitResult"}'

    {"message":"GAME OVER","sessionId":"2ad8f8430e3681c4dea8696ae19fb323","data":{"playerId":"kwailamchan@hotmail.com","sessionId":"2ad8f8430e3681c4dea8696ae19fb323","totalWordCount":80,"correctWordCount":78,"totalWrongGuessCount":231,"score":1329,"datetime":"2016-01-22 14:26:57"}}(hangman_client)hangman@vagrant-ubuntu-trusty-64:/hangman/hangman_client/hangman_client/bot2$
