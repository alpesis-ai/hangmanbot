import json
import requests

import client.settings as settings

def api_session(params):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(settings.REQUEST_URL, headers=headers, json=params)
    return json.loads(response.text)
