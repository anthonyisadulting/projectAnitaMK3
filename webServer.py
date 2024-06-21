from imutils.video import VideoStream
from flask import Response, Flask, render_template, redirect, url_for, Request, stream_with_context
import testdrive
import threading
import argparse
import datetime
import imutils
import time
import cv2

#'/dev/video0' probably need gst 
camera = cv2.VideoCapture(-1, 2)

app = Flask(__name__)

def generateFrame():
    while True:
        #read camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
        yield(b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/videofeed")
def videofeed():
    return Response(generateFrame(), mimetype = 'multipart/x-mixed-replace; boundary=frame')

@app.route("/stop")
def stopApp():

    testdrive.movement(0)

    return render_template("index.html")

@app.route("/forward")
def forwardApp():

    testdrive.movement(1)

    return render_template("index.html")

@app.route("/backward")
def backwardApp():

    testdrive.movement(2)

    return render_template("index.html")

@app.route("/left")
def leftApp():

    testdrive.movement(3)

    return render_template("index.html")

@app.route("/right")
def rightApp():

    testdrive.movement(4)

    return render_template("index.html")

@app.route("/lightMode")
def lightModeApp():

    testdrive.movement(5)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port = 80)