import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-private user-read-email playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative"

# Uses ClientAuth method since we want access to 'private' scopes
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Filter out the MM Playlists
playlists = sp.current_user_playlists(limit=50)['items']
mm_playlists = []
for playlist in playlists:
    if "MM:" in playlist['name']:
        mm_playlists.append(playlist)

all_songs = [] # contains just the song name
duplicates = [] # contains full track object

# Filter out all songs which appear multiple times in the MM playlists
for pl in mm_playlists: 
    for item in sp.playlist_items(pl['id'])['items']:
        if item['track']['name'] in all_songs:
            duplicates.append(item['track']['uri'])
        else:
            all_songs.append(item['track']['name'])

# Create the new playlist and add all duplicate tracks to it
created_playlist = sp.user_playlist_create(sp.current_user()['id'], "MM: The Hits")
add = sp.user_playlist_add_tracks(sp.current_user()['id'], created_playlist['id'], duplicates)

print('Created new playlist, populated with duplicate songs: ')
print(str(add))
