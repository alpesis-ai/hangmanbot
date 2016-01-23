import json
import requests


class HangmanServer(object):

    def __init__(self, requestUrl, playerId):
        self.requestUrl = requestUrl
        self.playerId = playerId

    def start_game(self):
        params = {'playerId': self.playerId, "action":"startGame"}
        return _connect_api(self.requestUrl, params)

    def next_word(self, sessionId):
        params = {'sessionId': sessionId, "action":"nextWord"}
        return _connect_api(self.requestUrl, params)

    def guess_word(self, sessionId, guess):
        params = {'sessionId': sessionId, "action":"guessWord", "guess": guess}
        return _connect_api(self.requestUrl, params)

    def get_result(self, sessionId):
        params = {'sessionId': sessionId, "action":"getResult"}
        return _connect_api(self.requestUrl, params)

    def submit_result(self, sessionId):
        params = {'sessionId': sessionId, "action":"submitResult"}
        return _connect_api(self.requestUrl, params)


def _connect_api(requestUrl, params):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(requestUrl, headers=headers, json=params)
    return json.loads(response.text)
