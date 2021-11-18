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

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

modsArr = []
modsDict = {}
#while scores:
#    for i in range(len(scores)):
#        if scores[i]["mods"] == scores[0]["mods"]:
#            modsDict[str(scores[0]["mods"])] += 1
#            del scores[i]

for i in range(len(scores)):
    if not scores[i]["mods"] in modsArr:
        modsArr.append(scores[i]["mods"])

for i in range(len(modsArr)):
    modsArrFormatted = listToString(modsArr[i])
    modsDict.update({modsArrFormatted: 0})
so = 0
#for each score
for i in range(len(scores)):
    #for each mod
    for ii in range(len(modsArr)):
        #check if the score has the mod
        if scores[i]["mods"] == modsArr[ii]:
            #find the current count on this mod
            value = modsDict.get(listToString(modsArr[ii])) + 1
            #lets goooo
            modsDict.update({   listToString(modsArr[ii]) : value   })
            value = 0
            

print(modsDict)    


