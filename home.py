# Team: 26
# Team Members: Jim O. Cabrera, Timothy Johnson, Andrea Sanchez, Geoffrey Vasaya
# Contributor: Timothy Johnson
# CST 205: Multimedia Design
# May 17, 2021 

from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import speech_recognition as sr

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def transcript():
    transcript = ""
    if request.method == "POST":

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None) #This var holds the sentence

    return render_template('home.html', transcript=transcript)