import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-top-read user-read-currently-playing streaming user-read-playback-position app-remote-control user-read-private user-read-email playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative user-library-read"


# Uses ClientAuth method since we want access to 'private' scopes
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# for seed in sp.recommendation_genre_seeds()['genres']:
#     if 'indie' in seed:
#         print(str(seed))

created_playlist = sp.user_playlist_create(sp.current_user()['id'], "MM: Funky Flavor")
suggestions = []
num_tries = 0
while len(suggestions) < 50:
    if num_tries >= 3:
        break
    for rec in sp.recommendations(seed_tracks=['3kFNbDzkKUlOkjd3gMrQLN','24G1PXBWoRgV0wDXZKwxzz','7eWGnKg4B44sbBPpQp4y2c','6Q8eZ3v4CzS8X1MjdXzd8M','7oGwQOTkMB9Sk3DIKJLd5F'], limit=50, min_energy=0.4, max_liveness=0.2)['tracks']:
        # if int(sp.artist(rec['artists'][0]['id'])['followers']['total']) < 500000:
      if rec['uri'] not in suggestions:
        suggestions.append(rec['uri'])
    num_tries = num_tries + 1

add = sp.user_playlist_add_tracks(sp.current_user()['id'], created_playlist['id'], suggestions)
