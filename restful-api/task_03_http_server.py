#!/usr/bin/python3
"""A simpleHTTP server and endpoints handling for API """


import http.server
import socketserver
import json


PORT = 8000


class MyFirstServer(http.server.BaseHTTPRequestHandler):
    "Class that defines endpoints handling with do_Get method"

    def do_GET(self):
        """do_GET method to manage endpoints handling"""

        if self.path == "/data":
            """/data endpoint handling"""
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
            self.wfile.flush() 
            """ensure to send data direcly after self.wfile.write
            call by flushing > must avoid some BrokenPipeError
            """

        elif self.path == "/status":
            """/status endpoint handling"""
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()

            message = "ok"
            self.wfile.write(message.encode("utf-8"))
            self.wfile.flush()

        else:
            """unknown endpoints handling"""
            self.send_response(404)
            self.send_header("content-type", "text/plain")
            self.end_headers()

            message = "404 Not Found: no '{}' endpoint".format(self.path)
            self.wfile.write(message.encode("utf-8"))
            self.wfile.flush()

with socketserver.TCPServer(("", PORT), MyFirstServer) as httpd:
    print("Serving on PORT {}".format(PORT))
    httpd.serve_forever()