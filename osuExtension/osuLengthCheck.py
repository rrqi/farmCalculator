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
r1 = requests.get('https://osu.ppy.sh/api/v2/users/' + str(userN) + '/scores/best?limit=50&offset=0', headers=headers)
r2 = requests.get('https://osu.ppy.sh/api/v2/users/' + str(userN) + '/scores/best?limit=50&offset=50', headers=headers)
j1 = json.loads(r1.text)
j2 = json.loads(r2.text)
jj = j1 + j2
ringtone = 0
tvSize = 0
normal = 0
long = 0
marathon = 0
for item in jj:
    mods = item['mods']
    exist = False
    for mod in mods:
        if(mod == "DT" or mod == "NC"):
            exist = True
    if(exist == True):
        if(item['beatmap']['total_length'] < 90):
            ringtone += 1
        elif(item['beatmap']['total_length'] < 180):
            tvSize += 1
        elif(item['beatmap']['total_length'] < 315):
            normal += 1
        elif(item['beatmap']['total_length'] < 540):
            long += 1
        else:
            marathon += 1
    else:
        if(item['beatmap']['total_length'] < 60):
            ringtone += 1
        elif(item['beatmap']['total_length'] < 120):
            tvSize += 1
        elif(item['beatmap']['total_length'] < 210):
            normal += 1
        elif(item['beatmap']['total_length'] < 360):
            long += 1
        else:
            marathon += 1
print("Amount of Ringtone Sized Maps: " + str(ringtone))
print("Amount of TV Sized Maps: " + str(tvSize))
print("Amount of Medium Sized Maps: " + str(normal))
print("Amount of Long Sized Maps: " + str(long))
print("Amount of Marathon Sized Maps: " + str(marathon))
    #print(json.dumps(item['beatmap']['version'], indent = 1))

