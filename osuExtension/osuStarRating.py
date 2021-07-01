import requests
import json
import sys

exec(open("osuAuth.py").read())
print(get_token()["access_token"])
headers = {
    'Authorization': 'Bearer ' + get_token()["access_token"]
}


userId = sys.argv[1]
theUser = requests.get('https://osu.ppy.sh/api/v2/users/' + userId, headers=headers)
user = json.loads(theUser.text)
userN = user['id']
r1 = requests.get('https://osu.ppy.sh/api/v2/users/' + str(userN) + '/scores/best?limit=50&offset=0', headers=headers)
r2 = requests.get('https://osu.ppy.sh/api/v2/users/' + str(userN) + '/scores/best?limit=50&offset=50', headers=headers)
j1 = json.loads(r1.text)
j2 = json.loads(r2.text)
jj = j1 + j2
under = 0
maps = []
count = 0
for item in jj:
    mods = item['mods']
    exist = False
    for mod in mods:
        if(mod == "DT" or mod == "NC" or mod == "HR"):
            exist = True
    if(exist == True):
        pass
    else:
        if(item['beatmap']['difficulty_rating'] < 6.00):
            under += 1
            maps.append(item['beatmapset']['title'])
            print(maps[count])
            count += 1
        else:
            pass
print("Amount of NM Maps under 6*: " + str(under))

    #print(json.dumps(item['beatmap']['version'], indent = 1))

