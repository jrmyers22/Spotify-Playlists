import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-currently-playing streaming user-read-playback-position app-remote-control user-read-private user-read-email playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative user-library-read"


# Uses ClientAuth method since we want access to 'private' scopes
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

print(sp.current_user_saved_episodes())
