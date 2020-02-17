from threading import Thread
import http.server
import socketserver
from functools import partial

from http.server import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    CRYPT = "password-1"
    connection_list = []

    def __init__(self, speaker, *args, **kwargs):
        self.speaker = speaker
        super().__init__(*args, **kwargs)

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        # decode incoming data // see if password is correct here!
        if post_data.decode('utf-8').__contains__("api_crypt="+self.CRYPT):
            data = post_data.decode('utf-8').split("&")

            # detemine source data
            if not self.client_address[0] in self.connection_list:
                self.speaker.say("New Server Connection From Address " + str(self.client_address[0]) + " PORT " + str(self.client_address[1]) )
                self.connection_list.append(self.client_address[0])

            for d in data:
                v = d.replace("+"," ")
                value = v.split("=")

                if value[0] == "api_rate":
                    self.speaker.setSpeed(float(value[1]))
                elif value[0] == "api_text":
                    self.speaker.say(value[1])
                elif value[0] == "api_volume":
                    self.speaker.setVolume(float(value[1]))
            self._set_response()

class server(Thread):

    PORT = 8000

    def __init__(self, speaker):
        super().__init__()
        self.speaker = speaker

    def run(self):
        server_address = ('localhost', self.PORT)
        httpd = HTTPServer(server_address, partial( S, self.speaker))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
