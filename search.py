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
filename = 'SearchAlbums_'+ date + '.txt'
result = 'SeachResult_'+ date +'.txt'
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
    
    response = sp.search('year:2022',type ='track',market = c)
    #while response:
    tracks = response['tracks']
    for item in tracks['items']:
        album = item['album']
        if album['release_date'] == '2022-08-18':
           
            if item['id'] not in ids: 
                
                print( item['name'], album['release_date'], album['total_tracks'], item['id'])
                
                newline = item['id'] +'%'+ item['name']+'%'+ str(album['total_tracks']) + ' \n'
                ids.append(item['id'])
                day_total = day_total + album['total_tracks']
                ### Store data
                total = open(result,'w')
                total.write(str(day_total))
                #### update database
                released = open(filename,'a')
                released.write(newline)
#except: 
    print( c , 'failed')




    '''
        if albums['next']:
            response = sp.next(albums)
        else:
            response = None
        time.sleep(1)'''

