import requests
import json


def jokes(f):
    
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt

f = r"https://official-joke-api.appspot.com/random_joke"
a = jokes(f)

print(a["setup"])
print(a["punchline"], "\n")