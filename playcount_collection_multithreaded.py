import numpy as np
import requests
import concurrent.futures
import os


playcount_url = "https://api.t4ils.dev/albumPlayCount?albumid="
artists_albums = np.load("artists_albums_clean.npy", allow_pickle=True).item()
artists_albums_tracks = np.load("artists_albums_clean.npy", allow_pickle=True).item()
responses = np.load("playcount_responses.npy", allow_pickle=True).item()
tuples_to_request = set([(artist_id, album_id) for artist_id in artists_albums.keys() for album_id in artists_albums[artist_id][
    "albums"].keys()]) - set(responses.keys())
errors = set()
total_iters = len(tuples_to_request)



def get_request(artist_id, album_id, index, try_number=0):
    global responses, futures, executor
    # make a request and get the data
    response = requests.api.get(playcount_url + album_id)
    if response.status_code == 200:
        responses[(artist_id, album_id)] = {"artist_id": artist_id, "discs": response.json()["data"]["discs"]}
        print("SUCCESS: " + str(index) + " of " + str(total_iters), flush=True)
    elif try_number > 2:
        print("TERMINAL ERROR: " +artist_id + " " + album_id, flush=True)
        print(response.content, flush=True)
        errors.add((artist_id, album_id))
        np.save("playcount_errors", errors)
    else:
        futures.append(executor.submit(get_request, artist_id, album_id, try_number+1))
        print("Trying again for albumid: " + album_id + " on error #: " + str(try_number), flush=True)
        print(response.content)
#
# print("Starting jobs", flush=True)
# executor = concurrent.futures.ThreadPoolExecutor(400)
# futures = [executor.submit(get_request, artist_id, album_id, index) for index, (artist_id, album_id) in enumerate(
#     tuples_to_request)]
# concurrent.futures.wait(futures)
# print("Saving")
# np.save("playcount_responses", responses)
# print("Finished getting responses")