import pyttsx3
from threading import Thread
from multiprocessing import Queue
import time
from textwrap import wrap

class speaker():
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
        self.converter.connect('started-word', self.onWord)

    def showAllVoices(self):
        self.voices = self.converter.getProperty('voices')

        for voice in self.voices:
            # to get the info. about various voices in our PC
            print("Voice:")
            print("ID: %s" %voice.id)
            print("Name: %s" %voice.name)
            print("Age: %s" %voice.age)
            print("Gender: %s" %voice.gender)
            print("Languages Known: %s" %voice.languages)

    def setVoice(self,voice_id):
        self.converter.setProperty('voice', voice_id)
        self.converter.runAndWait()

    def setSpeed(self,i):
        # in percent
        self.converter.setProperty('rate', i)

    def setVolume(self,i):
        # Set volume 0-1
        self.converter.setProperty('volume', i)

    def clear_queue(self):
        while not self.queue.empty():
            try:
                self.queue.get(False)
            except Empty:
                continue

    def say(self,s):
        if s == "stop":
            self.clear_queue()
            self.converter.stop()
            self.stopped = True

        else:
            self.queue.put(s)

    def start(self):
        
        self.run()

    def onWord(self, name, location, length):
        #print ('word', name, location, length)
        if self.stopped:
           self.converter.stop()

    def run(self):
        while True:
            i = 0
            while not self.queue.empty():
                s = self.queue.get()
                print()
                print(self.name+">",s)
                print()
                self.converter.say(s)
                self.converter.runAndWait()
            time.sleep(1) # sleep one second
