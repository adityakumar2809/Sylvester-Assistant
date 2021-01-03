import requests
import json


def get_random_advice():
    url = r'https://api.adviceslip.com/advice'
    advice_response = requests.get(url)
    advice_content = json.loads(advice_response.text)
    advice = advice_content['slip']['advice']
    return advice


if __name__ == "__main__":
    print(get_random_advice())