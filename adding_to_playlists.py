import numpy as np
import operator
import spotipy
import spotipy.util as util
import sys

sorted_track_list = np.load("sorted_track_list.npy", allow_pickle=True)
client_id = "04f1a97ae9a34db7b18fc358efa101ea"
client_secret = "5ac452808e714c658e1b3b69f8561331"
username = "th17aaap51n6ave8lq20jjkvi?si=fmq5aui1TFa17mUUyFB2jA"
redirect_uri = "https://www.google.com/"
#playlist_id = "4xaMwjsDWDKEC8OiQyOtI2"

# sorted_track_list = sorted(sorted_track_list, key=operator.itemgetter(0), reverse=True)
# np.save("sorted_track_list", sorted_track_list)
# sorted_track_list = [x for x in sorted_track_list if x[0] != "nan"]
# sorted_track_list = [x for x in sorted_track_list if x[0] != "inf" or int(x[1]) > 100000]
# sorted_track_list = sorted_track_list[:660000]
# np.save("sorted_track_list", sorted_track_list)
#['inf' '9806322' 'spotify:track:1djfwy9FvafpK4KhznjjeI' 'We Ready', Ride Wit Me Dirty South Style' 'Archie Eversole']

scope = 'playlist-modify-public user-library-read playlist-modify-private playlist-read-private'
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth=token)

to_add = []
curr_index = 0
for iter in range(100):
    to_add = []
    while(len(to_add) < 100):
        (iqr_quantile, playcount, track_uri, track_name, album_name, artist_name) = sorted_track_list[curr_index]
        curr_index += 1
        if artist_name not in artists_dict.keys():
            artists_dict[artist_name] = 0
        if artists_dict[artist_name] < artist_max_tracks:
            to_add.append(track_uri)
            artists_dict[artist_name] = artists_dict[artist_name] + 1
    result = sp.user_playlist_add_tracks(username, playlist_id, to_add)
    print("Added batch: " + str(iter) + " of 100")

print("Current index: " + str(curr_index))
print("FINISHED. ENJOY!!!!!")
