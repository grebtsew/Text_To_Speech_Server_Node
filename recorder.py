import pyttsx3
from gtts import gTTS
from datetime import datetime

"""
Use this file to save sample strings as video files
"""

# Write text to save here
theText = ""

now = datetime.now()

WAVE_OUTPUT_FILENAME ="recordings/"+ now.strftime("%d-%m-%Y_%H-%M-%S")+".mp3"
#Saving part starts from here 
tts = gTTS(text=theText, lang='en')
tts.save(WAVE_OUTPUT_FILENAME)
print("File saved!")