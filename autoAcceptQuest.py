#!/usr/bin/python3
import requests

url = "https://habitica.com/api/v3/groups/party"

# Change these two only
xapiuser = "YOUR_API_USER_ID"
xapikey = "YOUR_API_KEY"


xclient = "b1685e52-643e-481d-aa58-bde09c31444f-OpusC-habitica-automation"

headers = {'content-type': 'application/json',
        'x-api-user': xapiuser,
        'x-client': xclient,
        'x-api-key': xapikey}

response = requests.get(url, headers=headers)

responseJson = response.json()
quest = responseJson['data']['quest']

if not quest['active'] and not quest['members'][xapiuser]:
    print("gonna accept quest")
    questAccept = requests.post(url + "/quests/accept" , headers=headers)
    questAcceptResponse = questAccept.json()
    print(questAcceptResponse)

else:
    print("don't need to accept")
    print(quest)

