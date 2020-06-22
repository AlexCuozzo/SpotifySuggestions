
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from string import ascii_lowercase
import numpy as np
client_id = "04f1a97ae9a34db7b18fc358efa101ea"
client_secret = "5ac452808e714c658e1b3b69f8561331"
username = "th17aaap51n6ave8lq20jjkvi?si=fmq5aui1TFa17mUUyFB2jA"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


genre = "\"hip hop\""
data_dict = {} #np.load("hip_hop_artists.npy", allow_pickle=True).item()

limit = 50
#go through alphabet
for letter in ascii_lowercase:
    offset = 0
    hasNext = True
    while hasNext:
        try:
            artists = sp.search(letter + " genre:" + genre, type="artist", offset=offset, limit=limit)["artists"]
            hasNext = artists["next"] is not None
            offset += limit
            for artist in artists["items"]:
                name = artist["name"]
                popularity = artist["popularity"]
                followers =artist["followers"]["total"]
                id = artist["id"]
                data_dict[id] = (name, followers, popularity)
                print("Name: " + str(name) + " ID: " + str(id) + " Followers: " + str(followers) + " Popularity: " + str(popularity))
            np.save("hip_hop_artists", data_dict)
        except:
            break




