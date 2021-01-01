import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from decouple import config
import json

SPOTIPY_CLIENT_ID = config('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = config('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = config('SPOTIPY_REDIRECT_URI')

scope = [
    'user-library-read', 
    'user-read-recently-played', 
    'user-top-read', 
    'user-read-playback-position',
    'user-read-private',
    'user-read-playback-state',
    'user-modify-playback-state'
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

devices = sp.devices()
deviceID = devices['devices'][0]['id']

track = sp.current_user_playing_track()
artist = track['item']['artists'][0]['name']
track = track['item']['name']
if artist !="":
    print("Currently playing " + artist + " - " + track)
