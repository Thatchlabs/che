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
filename =  date + '.txt'
result = 'CA_Result'+ date +'.txt'
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
    try:
        day_total = day_total + int(fields[2].strip())
    except:
        print('failure at data point ',line)

albums = []
released_today = [] 
list_of_categories = []
data_dict = {}
no_of_uploads = 0
for c in country_codes:
    r = sp.categories(country = c)
    #while r:
    categories = r['categories']
    for i, item in enumerate(categories['items']):
        if item['id'] not in list_of_categories:
            list_of_categories.append(item['id'])
            try:
                response = sp.category_playlists(category_id = item['id'], country= c)      
                playlist = response['playlists']
                for j, jtem in enumerate(playlist['items']):
                    
                        tracks = sp.playlist_items(jtem['id'])
                        
                        for prack in tracks['items']:
                            try:     
                                qrack= prack['track']
                                track = qrack['album']
                                if track['release_date'] == date : # format "2022-08-18"
                                    if track['id'] not in ids:
                                        print(track['name'], track['release_date'], track['total_tracks'], track['id'])
                                        newline = track['id'] +'%'+ track['name']+'%'+ str(track['total_tracks']) + ' \n'
                                    
                                        
                                        ids.append(track['id'])
                                        day_total = day_total + int(track['total_tracks'])
                                        ### Store data
                                        total = open(result,'w')
                                        total.write(str(day_total))
                                        #### update database
                                        released = open(filename,'a')
                                        released.write(newline)
                                        
                                        
                                        
                                        no_of_uploads = no_of_uploads + int(track['total_tracks'])        
                                        
                            except:
                                qwe4e = 0
            except: 
                print ('id failure')
            print(day_total)
    print('Done with ', c ,' next country >>>>')
print("Total Number of Albums realesed today: " , day_total)
                    


