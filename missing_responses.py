import numpy as np
import requests
import concurrent.futures

# i = 0
# for artist_id, artist_data in artists_albums_playcounts.items():
#     for album_id, album_data in artist_data["albums"].items():
#         if "tracks" not in album_data.keys():
#             missing_responses.append((album_id, artist_id))
#     print("FINISHED ARTIST: " + str(i) + " of " + str(len(artists_albums_playcounts.keys())))
# np.save("missing_responses", missing_responses)

#
# missing_responses = np.load("missing_responses.npy", allow_pickle=True)
# extra_responses = {}
# playcount_url = "https://api.t4ils.dev/albumPlayCount?albumid="
# total_iters = len(missing_responses)
#
#
#
# def get_request(artist_id, album_id, index, try_number=0):
#     global responses, futures, executor
#     # make a request and get the data
#     response = requests.api.get(playcount_url + album_id)
#     if response.status_code == 200:
#         extra_responses[(artist_id, album_id)] = response.json()["data"]["discs"]
#         print("SUCCESS: " + str(index) + " of " + str(total_iters), flush=True)
#     elif try_number > 2:
#         print("TERMINAL ERROR: " +artist_id + " " + album_id, flush=True)
#         print(response.content, flush=True)
#     else:
#         futures.append(executor.submit(get_request, artist_id, album_id, try_number+1))
#         print("Trying again for albumid: " + album_id + " on error #: " + str(try_number), flush=True)
#         print(response.content)
#
# print("Starting jobs", flush=True)
# executor = concurrent.futures.ThreadPoolExecutor(400)
# futures = [executor.submit(get_request, artist_id, album_id, index) for index, (artist_id, album_id) in enumerate(missing_responses)]
# concurrent.futures.wait(futures)
# print("Saving")
# np.save("extra_responses", extra_responses)
# print("Finished getting responses")

