import numpy as np


# artists_and_albums = np.load("artists_and_albums.npy", allow_pickle=True).item()
# cleaned_artists_and_albums = np.load("artists_and_albums.npy", allow_pickle=True).item()
# for artist_id, artist in artists_and_albums.items():
#     cleaned_artists_and_albums[artist_id]["albums"] = {}
#     album_names = set()
#     to_add = {}
#     for album_id, (album_name, type) in artist["albums"].items():
#         if album_name not in album_names:
#             album_names.add(album_name)
#             to_add[album_id] = {"name": album_name, "type": type}
#     cleaned_artists_and_albums[artist_id]["albums"] = to_add
#
# np.save("artists_albums_clean", cleaned_artists_and_albums)
cleaned_artists_and_albums = np.load("artists_albums_clean.npy", allow_pickle=True).item()