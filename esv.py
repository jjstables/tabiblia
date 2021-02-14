import sys
import requests
import json

file = open('shh.json')
variables = json.loads(file.read())

API_KEY = variables["esvkey"]
API_URL = 'https://api.esv.org/v3/passage/text/'

def get_esv_text(passage):
    params = {
        'q': passage,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': True,
        'include-short-copyright': True,
        'include-passage-references': True
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    response = requests.get(API_URL, params=params, headers=headers)

    passages = response.json()['passages']

    return passages[0].strip() if passages else 'Error: Passage not found'
