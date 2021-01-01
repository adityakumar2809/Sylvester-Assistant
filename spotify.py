import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from decouple import config

SPOTIPY_CLIENT_ID = config('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = config('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = config('SPOTIPY_REDIRECT_URI')

scope = [
    'user-library-read', 
    'user-read-recently-played', 
    'user-top-read', 
    'user-read-playback-position'
]
scope = ' '.join(map(str, scope)) 

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        SPOTIPY_CLIENT_ID,
        SPOTIPY_CLIENT_SECRET,
        SPOTIPY_REDIRECT_URI,
        scope=scope
        )
    )

print(sp.current_user_recently_played(limit=1))
