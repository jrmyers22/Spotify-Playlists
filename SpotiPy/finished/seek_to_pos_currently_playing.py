import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-currently-playing streaming user-read-playback-position app-remote-control user-read-private user-read-email playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative"


# Uses ClientAuth method since we want access to 'private' scopes
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Changes the current position in the song to the halfway point
length = sp.current_user_playing_track()['item']['duration_ms']
sp.seek_track(int(length / 2))

