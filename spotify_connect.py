# spotify_connect.py
# !/usr/bin/env python

from secrets import CLIENT_ID, CLIENT_SECRET
import requests
from pprint import pprint

API_URL = 'https://api.spotify.com'
REQUEST_URL = 'https://accounts.spotify.com/authorize'
AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'authorization_code',
    'client id': CLIENT_ID,
    'secret': CLIENT_SECRET,
})

print(auth_response)

# auth_response_data = auth_response.json()

# pprint(auth_response_data)

# access_token = auth_response_data['access_token']
# print(access_token)