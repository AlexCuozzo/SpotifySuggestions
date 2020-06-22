import numpy as np


# artists_albums = np.load("artists_albums_clean.npy", allow_pickle=True).item()
#artists_albums_tracks = np.load("artists_albums_clean.npy", allow_pickle=True).item()
# print("LOADING RESPONSES")
# playcount_responses = np.load("playcount_responses.npy", allow_pickle=True).item()
# total_responses = len(playcount_responses.keys())
# i=0
# print("STARTING LOOP")
# for (artist_id, album_id), data in playcount_responses.items():
#     tracks = {}
#     for disc in data["discs"]:
#         for track in disc["tracks"]:
#             tracks[track["uri"]] = {"name": track["name"], "playcount": track["playcount"]}
#     artists_albums_tracks[artist_id]["albums"][album_id]["tracks"] = tracks
#     print("FINISHED ALBUM: " + str(i) + " of " + str(total_responses))
#     i+=1
# print("DATA COMPLETE: SAVING")
# #np.save("artists_albums_tracks", artists_albums_tracks)