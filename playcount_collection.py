import numpy as np
import requests
playcount_url = "https://api.t4ils.dev/albumPlayCount?albumid="
albums_dict = np.load("albums_dict_cleaned.npy", allow_pickle=True).item()
albums_playcounts = np.load("albums_playcounts.npy", allow_pickle=True).item()

i = 0
dict_length = len(list(albums_dict.keys()))

for (album_name, album_type, artist), album_id in albums_dict.items():
    #make a request and get the data
    albums_playcounts[album_id] = (album_name, album_type, artist, {})
    response = requests.api.get(playcount_url + album_id)
    if response.status_code == 200:
        data = response.json()["data"]
        for disc in data["discs"]:
            for track in disc["tracks"]:
                track_name = track["name"]
                track_playcount = track["playcount"]
                track_uri = track["uri"]
                albums_playcounts[album_id][3][track_name] = (track_uri, track_playcount)
        np.save("albums_playcounts", albums_playcounts)
        print("Album: " + album_name + " #"+str(i)+" of " + str(dict_length))
        i+=1
    else:
        print("BAD RESPONSE")
        print(album_id)
        print(album_name)