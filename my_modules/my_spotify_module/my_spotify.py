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


def getDeviceId(spotify_object):
    devices = spotify_object.devices()
    device_id = devices['devices'][0]['id']
    return device_id


def getFeaturedPlaylists(spotify_object):
    playlists = spotify_object.featured_playlists(limit=5)
    playlist_ids = [x['id'] for x in playlists['playlists']['items']]
    playlist_names = [x['name'] for x in playlists['playlists']['items']]
    return playlist_ids, playlist_names


def getUserPlaylists(spotify_object):
    playlists = spotify_object.current_user_playlists(limit=5)
    playlist_ids = [x['id'] for x in playlists['items']]
    playlist_names = [x['name'] for x in playlists['items']]
    return playlist_ids, playlist_names


def getTracksFromPlaylist(spotify_object, playlist_id):
    playlist = spotify_object.playlist(playlist_id)
    track_uris = [x['track']['uri'] for x in playlist['tracks']['items']]
    return track_uris


def getRecentlyPlayedTracks(spotify_object):
    recently_played_tracks = spotify_object.current_user_recently_played(limit=30)
    track_uris = [x['track']['uri'] for x in recently_played_tracks['items']]
    return track_uris


def getUserTopTracks(spotify_object):
    user_top_tracks = spotify_object.current_user_top_tracks(limit=30)
    track_uris = [x['uri'] for x in user_top_tracks['items']]
    return track_uris


def startPlayback(spotify_object, device_id, track_uris):
    spotify_object.start_playback(device_id, None, track_uris)


def pausePlayback(spotify_object, device_id):
    spotify_object.pause_playback(device_id)


def resumePlayback(spotify_object, device_id):
    spotify_object.start_playback(device_id)


def playNextTrack(spotify_object, device_id):
    spotify_object.next_track(device_id)


def playPreviousTrack(spotify_object, device_id):
    spotify_object.previous_track(device_id)


if __name__ == "__main__":
    spotify_object = setup()
    device_id = getDeviceId(spotify_object)

    # user_playlist_ids, user_playlist_names = getUserPlaylists(spotify_object)
    # playlist_track_uris = getTracksFromPlaylist(spotify_object, user_playlist_ids[1])

    # featured_playlist_ids = getFeaturedPlaylists(spotify_object)

    # recently_played_track_uris = getRecentlyPlayedTracks(spotify_object)
    
    # user_top_track_uris = getUserTopTracks(spotify_object)


    # startPlayback(spotify_object, device_id, track_uris)
    # pausePlayback(spotify_object, device_id)
    # resumePlayback(spotify_object, device_id)
    # playNextTrack(spotify_object, device_id)
    # playPreviousTrack(spotify_object, device_id)
