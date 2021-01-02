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
        print(e)
        print('Say that again please...')
        return None

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
        choosePlaylist()
    elif 'my recently played track' in query:
        print('my recently played track')
    elif 'my top track' in query:
        print('top')
    elif 'featured playlist' in query:
        print('featured')
    elif 'next track' in query:
        print('next')
    elif 'previous track' in query:
        print('previous')
    elif 'pause the track' in query:
        print('pause')
    elif 'resume the track' in query:
        print('resume')


def choosePlaylist():
    pass


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
