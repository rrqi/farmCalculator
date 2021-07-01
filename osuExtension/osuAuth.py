import requests

API_URL = 'httpa://osu.ppy.sh/api/v2'
TOKEN_URL = 'https://osu.ppy.sh/oauth/token'

def get_token():
    data = {
        'client_id': 8161,
        'client_secret': '5oZdzZclpCtmzc8OTiFZZguCcVvoyQfpwiFuAX01',
        'grant_type': 'client_credentials',
        'scope': 'public'
    }

    response = requests.post(TOKEN_URL, data=data)

    print(response.json())

get_token()
