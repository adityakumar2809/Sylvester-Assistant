import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from decouple import config
import json

SPOTIPY_CLIENT_ID = config('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = config('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = config('SPOTIPY_REDIRECT_URI')

scope = [
    'ugc-image-upload',
    'user-read-recently-played',
    'user-top-read',
    'user-read-playback-position',
    'user-read-playback-state',
    'user-modify-playback-state',
    'user-read-currently-playing',
    'app-remote-control',
    'streaming',
    'playlist-modify-public',
    'playlist-modify-private',
    'playlist-read-private',
    'playlist-read-collaborative',
    'user-follow-modify',
    'user-follow-read',
    'user-library-modify',
    'user-library-read',
    'user-read-email',
    'user-read-private'
]
scope = ' '.join(map(str, scope)) 

spotify_object = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        SPOTIPY_CLIENT_ID,
        SPOTIPY_CLIENT_SECRET,
        SPOTIPY_REDIRECT_URI,
        scope=scope
        )
    )
