import numpy as np
import operator
import spotipy
import spotipy.util as util
import sys
import bisect

client_id = "04f1a97ae9a34db7b18fc358efa101ea"
client_secret = "5ac452808e714c658e1b3b69f8561331"
username = "th17aaap51n6ave8lq20jjkvi?si=fmq5aui1TFa17mUUyFB2jA"
redirect_uri = "https://www.google.com/"
playlist_id = "5fSiRKnA61M9AejYDV6tpn"
scope = 'playlist-modify-public user-library-read playlist-modify-private playlist-read-private'
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth=token)

# print("LOADING TRACKS")
# artists_albums_tracks = np.load("artists_albums_tracks_stats.npy", allow_pickle=True).item()
#
# print("Got here")
#
# max_entries = 10000
# sortedList = []
# track_set = set()
# for artist_id, artist_data in artists_albums_tracks.items():
#     for album_id, album_data in artist_data["albums"].items():
#         if "tracks" not in album_data.keys():
#             continue
#         for track_uri, track_data in album_data["tracks"].items():
#             if "iqr_quantile" not in track_data.keys() or "playcount" not in track_data.keys():
#                 continue
#             playcount = int(track_data["playcount"])
#             iqr_quantile = float(track_data["iqr_quantile"])
#             if len(sortedList) < max_entries:
#                 if track_data["name"] not in track_set:
#                     bisect.insort(sortedList, (playcount, iqr_quantile, track_uri))
#                     track_set.add(track_data["name"])
#             elif playcount > sortedList[0][0]:
#                 sortedList.remove(sortedList[0])
#                 if track_data["name"] not in track_set:
#                     bisect.insort(sortedList, (playcount, iqr_quantile, track_uri))
#                     track_set.add(track_data["name"])
#
# print("SORTING AND SAVING")
# sortedList.sort(reverse=True) #get decreasing order of playcount
# np.save("most_popular_hip_hop", sortedList)
# sortedList.sort(key=operator.itemgetter(1), reverse=True)
# np.save("most_popular_outlier_hip_hop", sortedList)
# print("DONE")
track_list = list(np.load("most_popular_outlier_hip_hop.npy", allow_pickle=True))
to_add = []
curr_index = 0
for iter in range(10):
    to_add = []
    while(len(to_add) < 100):
        (playcount, iqr_quantile, track_uri) = track_list[curr_index]
        to_add.append(track_uri)
        curr_index += 1
    result = sp.user_playlist_add_tracks(username, playlist_id, to_add)
    print(result)
    print("Added batch: " + str(iter+1) + " of 100")
print("FINISHED. ENJOY!!!!!")
