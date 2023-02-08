from random import randint
import requests

def login(clientName=None, clientEmail=None):
    json = {
        "clientName": clientName,
        "clientEmail": clientEmail
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients', json=json)
    return response

def get_token():
    nr = randint(1,9999999)
    json = {
        "clientName": 'Costel',
        "clientEmail": f'emailValid{nr}@mailinator.com'
    }

    response = requests.post('https://simple-books-api.glitch.me/api-clients', json=json)
    return response.json()['accessToken']