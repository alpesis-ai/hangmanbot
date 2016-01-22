import json
import requests


class HangmanServer(object):

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
        headers = {'Content-Type': 'application/json'}
        params = {'sessionId': sessionId, "action":"submitResult"}
        response = requests.post(self.requestUrl, headers=headers, json=params)
        return json.loads(response.text)
