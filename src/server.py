from threading import Thread
from functools import partial
import json
from jsonschema import validate, ValidationError, Draft7Validator
from http.server import BaseHTTPRequestHandler, HTTPServer
from speaker import logger


class S(BaseHTTPRequestHandler):
    PASSWORD = "password-1"
    connection_list = []
    schema = None

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

                if self.schema is None:
                    with open("./template/template.json", "r") as f:
                        self.schema = json.load(f)
                # Make sure request has correct format
                data = self.validate_request(data)

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

    def validate_request(self, data: dict) -> dict:
        """
        Validate incoming JSON against template.json schema.
        - Ensures required fields exist
        - Inserts default values for missing optional fields
        Returns the validated and completed data dict.
        """
        # Apply defaults from schema
        for prop, rules in self.schema.get("properties", {}).items():
            if "default" in rules and prop not in data:
                data[prop] = rules["default"]

        # Validate with schema
        validator = Draft7Validator(self.schema)
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
        if errors:
            for error in errors:
                print(f"❌ Invalid JSON: {error.message}")
            raise ValidationError("Incoming JSON failed validation")

        return data


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
