import time
import json
from collections import deque

import requests

import settings
import dictionary
import patterns

import nextword
import guessword
import getresult

import log.files

class HangmanClient(object):

    def __init__(self, requestUrl, playerId):
        self.requestUrl = requestUrl
        self.playerId = playerId

    def start_game(self):
        headers = {'Content-Type': 'application/json'}
        params = {'playerId': self.playerId, "action":"startGame"}
        response = requests.post(self.requestUrl, headers=headers, json=params)
        return json.loads(response.text)

    def next_word(self, sessionId):
       
        headers = {'Content-Type': 'application/json'}
        params = {'sessionId': sessionId, "action":"nextWord"}
        response = requests.post(self.requestUrl, headers=headers, json=params)
        return json.loads(response.text)

    def guess_word(self, sessionId, guess):
        headers = {'Content-Type': 'application/json'}
        params = {'sessionId': sessionId, "action":"guessWord", "guess": guess}
        response = requests.post(self.requestUrl, headers=headers, json=params)
        return json.loads(response.text) 

    def get_result(self, sessionId):
        headers = {'Content-Type': 'application/json'}
        params = {'sessionId': sessionId, "action":"getResult"}
        response = requests.post(self.requestUrl, headers=headers, json=params)
        return json.loads(response.text)

    def submit_result(self, sessionId):
        pass
    

def main():


    hangman_client = HangmanClient(settings.REQUEST_URL, settings.PLAYER_ID)
    session = hangman_client.start_game()
    if session['message'] == 'THE GAME IS ON':

        counter = 1
        while counter <= session['data']['numberOfWordsToGuess']:

            print "#####################################"
            print "# COUNTER: %s" % counter
            print "#####################################"
            time.sleep(1)

            sessionId = session['sessionId']
            word, wordLength, unknownLetters = nextword.next_word(hangman_client, sessionId)
            if unknownLetters > 0:
                unknownLetters, guessedWord = guessword.guess_word(hangman_client, sessionId, wordLength, unknownLetters)
                print unknownLetters, guessedWord
                log.files.log_words(guessedWord)
                if unknownLetters == 0:
                    result = getresult.get_result(hangman_client, session['sessionId'])
                    counter += 1
                    continue

        #best_score = get_best_score()
        #if result['data']['score'] > bestScore:
        #    save_score()
        #    submit_result()

    else:
        raise session['message']


if __name__ == '__main__':
    main()
