from threading import Thread

class console(Thread):

    def __init__(self, speaker):
        super().__init__()
        self.speaker = speaker

    def run(self):
        while True:
            s = input()
            self.speaker.say(s)
