import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from decouple import config
import json


def setup():

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

    return spotify_object


def get_device_id(spotify_object):
    devices = spotify_object.devices()
    device_id = devices['devices'][0]['id']
    return device_id


def get_user_playlists(spotify_object):
    playlists = spotify_object.current_user_playlists(limit=5)
    playlist_ids = [x['id'] for x in playlists['items']]
    return playlist_ids

def get_tracks_from_playlist(spotify_object, playlist_id):
    playlist = spotify_object.playlist(playlist_id)
    track_uris = [x['track']['uri'] for x in playlist['tracks']['items']]
    # print(json.dumps(playlist['tracks']['items'], indent=4, sort_keys=True))
    print(track_uris)

# track = spotify_object.current_user_playing_track()
# artist = track['item']['artists'][0]['name']
# track_name = track['item']['name']
# if artist !="":
#     print("Currently playing " + artist + " - " + track_name)

# track_uri = track['item']['uri']
# print(track_uri)

# spotify_object.start_playback(deviceID, None, [track_uri])


if __name__ == "__main__":
    spotify_object = setup()
    device_id = get_device_id(spotify_object)
    playlist_ids = get_user_playlists(spotify_object)
    get_tracks_from_playlist(spotify_object, playlist_ids[1])
