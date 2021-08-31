import requests
import json
import sys

exec(open("osuAuth.py").read())
headers = {
    'Authorization': 'Bearer ' + get_token()["access_token"]
}

userId = sys.argv[1]
theUser = requests.get('https://osu.ppy.sh/api/v2/users/' + userId, headers=headers)
user = json.loads(theUser.text)
userN = user['id']

scores = json.loads(requests.get('https://osu.ppy.sh/api/v2/users/' + str(userN) + '/scores/best?limit=100', headers=headers).text)

modsDict = {}
while scores:
    for i in range(len(scores)):
        if scores[i]["mods"] == scores[0]["mods"]:
            modsDict[str(scores[0]["mods"])] += 1
            del scores[i]
print(modsDict)

