
# importing the requests library
import requests
import time
import json

# defining the api-endpoint
API_ENDPOINT = "http://localhost:8000"

CRYPT = "password-1"

TEXT_TO_READ = "This example explains how to send data to the text to speech server node, feel free to play around with it! Have a good day!."

# data to be sent to api
data = {
        'api_rate':150,
        'api_volume':0.7,
        'api_text':TEXT_TO_READ,
        'api_crypt':CRYPT}


while True:
    print("Sending our POST request to server ...")
    print(API_ENDPOINT, data)
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = json.dumps(data))

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)

    time.sleep(15)
