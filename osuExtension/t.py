import requests
import json
import sys

#Charles
exec(open("osuAuth.py").read())
headers = {
    'Authorization': 'Bearer ' + get_token()["access_token"]
}


userId = sys.argv[1]
theUser = requests.get('https://osu.ppy.sh/api/v2/users/' + userId, headers=headers)
user = json.loads(theUser.text)
userN = user['id']

scores = json.loads(requests.get('https://osu.ppy.sh/api/v2/users/' + str(userN) + '/scores/best?limit=100', headers=headers).text)

spinners = 0
mapspinners = 0
for i in range(len(scores)):
        mapspinners = scores[i]["beatmap"]["count_spinners"]
        if "SO" in scores[i]["mods"]:
            mapspinners = 0
        spinners += mapspinners

print("there are "+str(spinners)+" spinners in this person's top 100")





