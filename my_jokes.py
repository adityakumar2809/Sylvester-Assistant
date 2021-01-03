import requests
import json


def getRandomJoke():
    url = r'https://official-joke-api.appspot.com/random_joke'
    joke_response = requests.get(url)
    joke_content = json.loads(joke_response.text)
    return joke_content


if __name__ == "__main__":
    getRandomJoke()