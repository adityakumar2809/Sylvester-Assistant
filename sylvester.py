import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import winsound

import spotify

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
spotify_object = spotify.setup()

number_dict = {
    'first': 0,
    'second': 1,
    'third': 2,
    'fourth': 3,
    'fifth': 4,
}


def beep():
    freq = 800
    duration = 700
    winsound.Beep(freq, duration)


def speak(audio):
    """Takes a string and outputs it through default speakers"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """Speaks the greeting based on the current system time"""

    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak('Good Morning Aditya Sir!')
    elif hour >= 12 and hour < 17:
        speak('Good Afternoon Aditya Sir!')
    elif hour >= 17 and hour < 22:
        speak('Good Evening Aditya Sir!')
    else:
        speak('Hello Aditya Sir!')
    speak('I am Sylvester. I am here to help you')


def takeCommand():
    """Takes microphone input and returns corresponding String"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        beep()
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en-in')
        print(f'User said: {query}')
    except Exception as e:
        speak('Say that again please...')
        print('Say that again please...')
        return takeCommand()

    return query


def searchWikipedia(query):
    """Search in wikipedia for a given query string"""
    speak('Searching Wikipedia...')
    search_string = query.replace('wikipedia', '')
    results = wikipedia.summary(search_string, sentences=2)
    speak(f"According to Wikipedia, {results}")


def exploitSpotify(query):
    """Decide which action to be performed in spotify module"""
    if 'my playlist' in query:
        choosePlaylist('user')
    elif 'my recently played track' in query:
        playRecentlyPlayedTracks()
    elif 'my top track' in query:
        playTopTracks()
    elif 'featured playlist' in query:
        choosePlaylist('featured')
    elif 'next track' in query:
        print('next')
        # spotify.play_next_track(
        #     spotify_object, 
        #     spotify.get_device_id(spotify_object)
        # )
    elif 'previous track' in query:
        print('previous')
        # spotify.play_previous_track(
        #     spotify_object, 
        #     spotify.get_device_id(spotify_object)
        # )
    elif 'pause the track' in query:
        print('pause')
        # spotify.pause_playback(
        #     spotify_object, 
        #     spotify.get_device_id(spotify_object)
        # )
    elif 'resume the track' in query:
        print('resume')
        # spotify.resume_playback(
        #     spotify_object, 
        #     spotify.get_device_id(spotify_object)
        # )


def playTrackFromUris(track_uris):
    print(track_uris)
    # spotify.start_playback(
    #     spotify_object,
    #     spotify.get_device_id(spotify_object),
    #     track_uris
    # )


def choosePlaylist(query):
    """Choose a playlist from a given list"""
    if 'user' in query:
        playlist_ids, playlist_names = spotify.get_user_playlists(
            spotify_object
        )
    elif 'featured' in query:
        playlist_ids, playlist_names = spotify.get_featured_playlists(
            spotify_object
        )
    if len(playlist_names) > 0:
        speak('Please choose the playlist from the following options')
        for i in range(len(playlist_names)):
            speak(playlist_names[i])
        selected_playlist_index = takeCommand()
        selected_playlist_index = number_dict[selected_playlist_index]
        speak(
            f'Playing {playlist_names[selected_playlist_index]}'
        )
        playTracksFromPlaylist(playlist_ids[selected_playlist_index])
    else:
        speak('Sorry Sir. No playlists available.')


def playTracksFromPlaylist(playlist_id):
    """Play tracks of a given playlist id"""
    playlist_track_uris = spotify.get_tracks_from_playlist(
        spotify_object,
        playlist_id
    )
    playTrackFromUris(playlist_track_uris)


def playRecentlyPlayedTracks():
    """Play tracks which were recently played by the user"""
    recently_played_track_uris = spotify.get_recently_played_tracks(
        spotify_object
    )
    playTrackFromUris(recently_played_track_uris)


def playTopTracks():
    """Play top tracks of the user"""
    top_track_uris = spotify.get_user_top_tracks(
        spotify_object
    )
    playTrackFromUris(top_track_uris)


def executeCommand(query):
    """Decide the action to be performed based on query string"""
    if 'wikipedia' in query:
        searchWikipedia(query)
    elif 'open youtube' in query:
        webbrowser.open('https://www.youtube.com')
    elif 'spotify' in query:
        exploitSpotify(query)
    elif 'sleep' in query:
        speak('We will meet again soon. Going to sleep.')
        return False
    return True


if __name__ == "__main__":
    # wishMe()
    continue_listening = True
    while continue_listening:
        query = takeCommand()
        if query:
            query = query.lower()
            continue_listening = executeCommand(query)
