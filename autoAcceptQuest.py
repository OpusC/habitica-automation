#!/usr/bin/python3
import requests

url = "https://habitica.com/api/v3/groups/party"

xapiuser = ""

xclient =  ""

xapikey = ""

headers = {'content-type': 'application/json',
        'x-api-user': xapiuser,
        'x-client': xclient,
        'x-api-key': xapikey}

response = requests.get(url, headers=headers)

responseJson = response.json()
quest = responseJson['data']['quest']

if not quest['active'] and not quest['members'][xapiuser]:
    print("gonna accept quest")
else:
    print("don't need to accept")
    print(quest)

