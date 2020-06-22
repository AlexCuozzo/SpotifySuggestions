
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from string import ascii_lowercase
import numpy as np
import concurrent.futures
client_id = "04f1a97ae9a34db7b18fc358efa101ea"
client_secret = "5ac452808e714c658e1b3b69f8561331"
username = "th17aaap51n6ave8lq20jjkvi?si=fmq5aui1TFa17mUUyFB2jA"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)




artists = np.load("hip_hop_artists.npy", allow_pickle=True).item()
artists_and_albums = np.load("artists_and_albums.npy", allow_pickle=True).item()
limit = 50

def getAlbumsThread(artist_id):
    global artists_and_albums, limit, sp
    offset = 0
    artist_albums = {}
    hasNext = True
    artist_name, followers, popularity = artists[artist_id]
    if artist_id in set(artists_and_albums.keys()):
        return
    while hasNext:
        try:
            albums = sp.artist_albums(artist_id, limit=limit, offset=offset)
            hasNext = albums["next"] is not None
            offset += limit
            for album in albums["items"]:
                album_type = album["album_type"]
                album_id = album["id"]
                album_name = album["name"]
                if (album_name, album_type) not in artist_albums:
                    artist_albums[album_id] = (album_name, album_type)
                #print("Artist: " + artist_name + " Album: " + album_name + " AlbumID: " + album_id, flush=True)
        except:
            print("ERROR", flush=True)
            break
    artists_and_albums[artist_id] = {"artist_name":artist_name, "followers":followers, "popularity":popularity, "albums":artist_albums}
    np.save("artists_and_albums", artists_and_albums)
    print("Artist Complete: " + artist_name, flush=True)

executor = concurrent.futures.ThreadPoolExecutor(10)
futures = [executor.submit(getAlbumsThread, aid) for aid in list(artists.keys())]
concurrent.futures.wait(futures)

print("Finished")


