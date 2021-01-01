import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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
    speak('I am Jarvis. I am here to help you')


def takeCommand():
    """Takes microphone input and returns corresponding String"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        query = recognizer.recognize_google(audio, language='en-in')
        print(f'User said: {query}')
    except Exception as e:
        print('Say that again please...')
        return None

    return query


def executeCommand(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        search_string = query.replace('wikipedia', '')
        results = wikipedia.summary(search_string, sentences=2)
        speak(f"According to Wikipedia, {results}")


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        executeCommand(query)
