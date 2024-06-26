from threading import Thread
from functools import partial
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from speaker import logger


class S(BaseHTTPRequestHandler):
    PASSWORD = "password-1"
    connection_list = []

    def __init__(self, speaker, *args, **kwargs):
        self.speaker = speaker
        super().__init__(*args, **kwargs)

    def _set_response(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS, HEAD, GET")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_HEAD(self):
        self._set_response()

    def do_OPTIONS(self):
        self._set_response()

    def do_POST(self):
        # print(self.client_address,self.headers)

        if self.headers["Content-Length"]:

            # <--- Gets the size of data
            content_length = int(self.headers["Content-Length"])
            # <--- Gets the data itself
            post_data = self.rfile.read(content_length)

            # decode incoming data // see if password is correct here!
            try:

                data = json.loads(post_data.decode("utf-8"))

                if data["password"]:
                    if data["password"] == self.PASSWORD:

                        # detemine source data
                        if not self.client_address[0] in self.connection_list:
                            self.speaker.say(
                                "New Server Connection From Address "
                                + str(self.client_address[0])
                                + " PORT "
                                + str(self.client_address[1])
                            )
                            self.connection_list.append(self.client_address[0])

                        self.speaker.queue.put(data)

            except Exception as e:
                logger.error("SERVER ERROR: ", str(e))
        self._set_response()


class server(Thread):

    PORT = 8000

    def __init__(self, speaker):
        super().__init__()
        self.speaker = speaker

    def run(self):
        server_address = ("localhost", self.PORT)
        httpd = HTTPServer(server_address, partial(S, self.speaker))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
