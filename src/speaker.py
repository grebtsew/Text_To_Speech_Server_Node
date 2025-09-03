import pyttsx3
from threading import Thread
from multiprocessing import Queue
import time
from textwrap import wrap
import logging
import pygame
import os

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler("tts_system_log.log")
file_handler.setLevel(logging.DEBUG)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


class speaker:
    """
    The speaker class handles read requests
    """

    queue = Queue()
    TEXT_LIMIT_SIZE = 5
    stopped = False

    def __init__(self):
        super().__init__()
        self.converter = pyttsx3.init()
        self.thread_stopped = False
        self.name = "System"
        self.setSpeed(150)
        self.setVolume(0.7)
        self.converter.connect("started-word", self.onWord)
        self.showAllVoices()

    def showAllVoices(self):
        self.voices = self.converter.getProperty("voices")

        for voice in self.voices:
            # to get the info. about various voices in our PC
            logger.info("Voice:")
            logger.info("ID: %s" % voice.id)
            logger.info("Name: %s" % voice.name)
            logger.info("Age: %s" % voice.age)
            logger.info("Gender: %s" % voice.gender)
            logger.info("Languages Known: %s" % voice.languages)

    def setVoice(self, voice_id):
        self.converter.setProperty("voice", voice_id)
        self.converter.runAndWait()

    def setSpeed(self, i):
        # in percent
        self.converter.setProperty("rate", i)

    def setVolume(self, i):
        # Set volume 0-1
        self.converter.setProperty("volume", i)

    def clear_queue(self):
        while not self.queue.empty():
            try:
                self.queue.get(False)
            except Exception:
                continue

    def say(self, s):
        if s == "stop":
            self.clear_queue()
            self.converter.stop()
            self.stopped = True
        else:
            data = {
                "api_rate": 150,
                "api_volume": 0.7,
                "api_voice": self.converter.getProperty("voice"),
                "api_text": s,
                "password": "password-1",
            }

            self.queue.put(data)

    def start(self):

        self.run()

    def onWord(self, name, location, length):
        # print ('word', name, location, length)
        if self.stopped:
            self.converter.stop()

    def play_mp3(self, path: str, volume: float):
        """Spelar upp en MP3-fil med pygame."""
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()

        print(f"Spelar: {path} med volym {volume*100:.0f}%")

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

    def run(self):
        while True:
            while not self.queue.empty():

                data = self.queue.get()
                if "api_voice" in data:
                    logger.info(f" Voice changed {data['api_voice']} ")
                    self.setVoice(data["api_voice"])

                if "api_rate" in data:
                    logger.info(f" Rate changed {data['api_rate']} ")
                    self.setSpeed(float(data["api_rate"]))

                if "api_volume" in data:
                    logger.info(f" Volume changed {data['api_volume']} ")
                    self.setVolume(float(data["api_volume"]))

                if "api_text" in data:

                    logger.info(f"{self.name} > {data['api_text']}")

                    if "api_tune" in data and os.path.isfile(data["api_text"]):
                        # Perform playing music here
                        try:
                            self.play_mp3(data["api_text"], float(data["api_volume"]))
                        except Exception as e:
                            pass
                    else:
                        # Perform speak command here
                        self.converter.say(data["api_text"])
                        self.converter.runAndWait()

            time.sleep(1)  # sleep one second
