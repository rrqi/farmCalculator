import requests
import json
import sys

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4MTYxIiwianRpIjoiNTBmNjhmYzIxOGM3YWQ1ZjM3NjE4ZmJlZjBhM2VmN2I2YWU5ZjM1MjY0NGM0ODQxYmJkMDgwMmEwOTdlNjljOTI2YzI0NTRhODY1OTcwNGQiLCJpYXQiOjE2MjQ4NTExNDUuOTk5MDEsIm5iZiI6MTYyNDg1MTE0NS45OTkwMTIsImV4cCI6MTYyNDkzNzU0NS45OTM1MzUsInN1YiI6IiIsInNjb3BlcyI6WyJwdWJsaWMiXX0.VAFmLQoBiX_MRv14osXSuZUsOXzqknJ31uC6kGDjmCTSqL6j1TufPfeYbWFEEMr2DjkHtphFcd2y9U_uzy_nNQtccb4sGXZAgNrCM4hYj5PqMcR3yNOtyBb3eryDvFYjSGDulci4IQwfBN_djt6Y_9RCSf-2lCGlrg9YgfFgijr172vEaa5pXck3UVGyBm2qRxk2YrHfjREmhlJ3yKL58sspQ04yzfGm4BvNDYU2_MDqyEOzmDFPwJ5F3CgJ3pgA-e63T3dHJpy4rGVqyAMW64He8b-C-48tRdKpZSBF6lR7kaS0lO8VNN1QNHMCTQom7dD-jh-5tAABbLY5NVkthXXerfbnAMgQUrov47LZei17EBnhFOh3DPuK96bIreybeiXujHATsykAPrRCSLC58QZb2INmeofOy0BmOkRyp_w7ogZJFYg6F2XFyJU-fATSIpzK7oOwm1FwDnculGBmR13HZFarrwpVGOl3RVSGrfgo_QdVzVqr6yr5pdff0QNZNwEGe_esEwG9fmm7YDIuf8Teqc3uv__g2WK9zS_nzsTiWhAADdONSZuLfBmg0K5ZLeq4z03yUoEm9aBmEr98jryNXw_j830BnO7AP8fCdirqdYfVBcCv3fYVSf_RjeKbH5bZcv9VF2MJ5TpzMhfZb6vfwHFlO1HST_l-c9j0VdI'
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

