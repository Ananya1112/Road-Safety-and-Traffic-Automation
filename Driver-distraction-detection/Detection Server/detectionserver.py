#!/usr/bin/python3

"""
Very simple HTTP server in python (Updated for Python 3.7)
Usage:
    ./detectionserver.py
Send a GET request:
    curl http://localhost:8000
Send a HEAD request:
    curl -I http://localhost:8000
Send a POST request:
    curl -d "foo=bar&bin=baz" http://localhost:8000
"""
import cgi
import cv2
import numpy
import base64
import os
import dlib
from http.server import HTTPServer, BaseHTTPRequestHandler
from detector import DrowsinessDetector

class TestDetectionServer(BaseHTTPRequestHandler):
    detector = DrowsinessDetector()

    def __init__(self, request, client_address, server):
        print("Constructor called")
        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def _set_headers(self, responseCode):
        self.send_response(responseCode)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        return message.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers(200)
        self.wfile.write(self._html("WELCOME TO OUR DROWSINESS DETECTOR"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        print('Post!')

        response = {"You are drowsy": True}

        ## Save file temporarily
        tmpFile = open("tmp.mp4", 'wb')
        tmpFile.write(self.rfile.read(int(self.headers["content-length"])))
        print("Bytes read: ", self.headers["content-length"])

        tmpFile.close()
        ## Split video file into frames
        vidObj = cv2.VideoCapture("tmp.mp4")
        count = 0
        success = 1

        errored = False

        while success:
            success, image = vidObj.read()
            if success != 1:
                break

            if count % 5 == 0:
                try:
                    cv2.imwrite("tmpFrame.jpg", image)
                    img = dlib.load_grayscale_image("tmpFrame.jpg")
                    appearsDrowsy = TestDetectionServer.detector.areEyesClosed(img)

                    print(appearsDrowsy)
                    print("current consecutive drowsy frames: ", TestDetectionServer.detector.getNumberConsecutiveDrowsyFrames())
                    if appearsDrowsy != None:
                        if not appearsDrowsy:
                            TestDetectionServer.detector.resetNumberConsecutiveDrowsyFrames()

                        if(TestDetectionServer.detector.isDrowsy()):
                            response["drowsy"] = True
                            break

                    if os.path.exists("tmpFrame.jpg"):
                        os.remove("tmpFrame.jpg")

                except Exception as e:
                    errored = True
                    print(e)
                    break

            count += 1
        print(count)

        ## Remove tmp file
        #if os.path.exists("tmp.mpg"):
        #    os.remove("tmp.mpg")

        if errored:
            self._set_headers(500)
        else:
            self._set_headers(200)

        print(response)
        self.wfile.write(self._html(str(response)))

def run(server_class=HTTPServer, handler_class=TestDetectionServer, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting http server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
	run(addr = "", port = 8000)
