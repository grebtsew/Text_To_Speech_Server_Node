# importing the requests library
import requests
import time
import json
import pyttsx3
import random

# defining the api-endpoint
API_ENDPOINT = "http://localhost:8000"


TEXT_TO_READ = "This example explains how to send data to the text to speech server node, feel free to play around with it! Have a good day!."

# data to be sent to api
data = {
    "api_rate": 150,
    "api_volume": 0.7,
    "api_text": TEXT_TO_READ,
    "password": "password-1",
}

requests.post(url=API_ENDPOINT, data=json.dumps(data))

converter = pyttsx3.init()
converter.getProperty("voices")
voices = converter.getProperty("voices")


i = 0
while True:
    random_index = random.randint(0, len(voices) - 1)

    data = {
        "api_rate": random.randint(50, 200),
        "api_volume": random.uniform(0.5, 0.7),
        "api_voice": voices[random_index].id,
        "api_text": str(i),
        "api_tune": False,
        "password": "password-1",
    }

    print("Sending our POST request to server ...")
    print(API_ENDPOINT, data)
    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=json.dumps(data))

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s" % pastebin_url)

    time.sleep(5)
    i += 1
