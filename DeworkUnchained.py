import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="cf442a032ca744868068d88ddd70ba5b",
                                                           client_secret="e5c291939f094a58a9dbde370026ed2b"))


# shows artist info for a URN or URL
#all spotify contries 
country_codes = [
        "AD",
        "AR",
        "AU",
        "AT",
        "BE",
        "BO",
        "BR",
        "BG",
        "CA",
        "CL",
        "CO",
        "CR",
        "CY",
        "CZ",
        "DK",
        "DO",
        "EC",
        "SV",
        "EE",
        "FI",
        "FR",
        "DE",
        "GR",
        "GT",
        "HN",
        "HK",
        "HU",
        "IS",
        "ID",
        "IE",
        "IT",
        "JP",
        "LV",
        "LI",
        "LT",
        "LU",
        "MY",
        "MT",
        "MX",
        "MC",
        "NL",
        "NZ",
        "NI",
        "NO",
        "PA",
        "PY",
        "PE",
        "PH",
        "PL",
        "PT",
        "SG",
        "ES",
        "SK",
        "SE",
        "CH",
        "TW",
        "TR",
        "GB",
        "US",
        "UY"]
x = 0
ids = []
day_total = 0
date = input(("Release Date: "))
filename = date + '.txt'
result = 'Result'+ date +'.txt'
#Open file
try:
    db = open(filename,'r').readlines()
except:
    opener = open(filename,'w')
    db = open(filename,'r').readlines()
    x =1
for line in db:
    fields= line.split('%')
    ids.append(fields[0]) 
    day_total = day_total + int(fields[2].strip())

if x == 1:
    opener.close()

for c in country_codes:
    try:
        response = sp.new_releases(c)
        #while response:
        albums = response['albums']
        for i, item in enumerate(albums['items']):
            if item['release_date'] == date: #Format = 2022-08-18
                if item['id'] not in ids: 
                    print(albums['offset'] + i, item['name'], item['release_date'], item['total_tracks'], item['id'])
                    
                    newline = item['id'] +'%'+ item['name']+'%'+ str(item['total_tracks']) + ' \n'
                    ids.append(item['id'])
                    day_total = day_total + item['total_tracks']
                    ### Store data
                    total = open(result,'w')
                    total.write(str(day_total))
                    #### update database
                    released = open(filename,'a')
                    released.write(newline)
    except: 
        print( c , 'failed')




    '''
        if albums['next']:
            response = sp.next(albums)
        else:
            response = None
        time.sleep(1)'''

