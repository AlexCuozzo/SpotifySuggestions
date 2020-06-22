import numpy as np
artists_albums_playcounts = np.load("artists_albums_tracks.npy", allow_pickle=True).item()
sorted_track_list = []
total_iterations = len(artists_albums_playcounts.keys())

quantiles = (0.25,0.75)
i = 0
for artist_id, artist_data in artists_albums_playcounts.items():
    counts = []
    for album_id, album_data in artist_data["albums"].items():
        if "tracks" not in album_data.keys():
            continue
        for track_uri, track_data in album_data["tracks"].items():
            counts.append(int(track_data["playcount"]))
    if len(counts) < 2:
        continue
    low, high = np.quantile(counts, quantiles)
    iqr = high-low
    for album_id, album_data in artist_data["albums"].items():
        if "tracks" not in album_data.keys():
            continue
        for track_uri, track_data in album_data["tracks"].items():
            iqr_quantile = (float(track_data["playcount"]) - high)/iqr
            track_data["iqr_quantile"] = iqr_quantile
            sorted_track_list.append((iqr_quantile, track_data["playcount"], track_uri, track_data["name"], album_data["name"], artist_data["artist_name"]))
    print("FINISHED ARTIST: " + artist_data["artist_name"] + "     " + str(i) + " of " + str(total_iterations))
    i+=1

#np.save("artists_albums_tracks_stats", artists_albums_playcounts)
#np.save("sorted_track_list", sorted_track_list)


