# Team: 26
# Team Members: Jim O. Cabrera, Timothy Johnson, Andrea Sanchez, Geoffrey Vasaya
# Contributor: Timothy Johnson
# CST 205: Multimedia Design
# May 17, 2021 

from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import speech_recognition as sr
import requests, json

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


#Duplicated code for simplicity, fully commented code on library.py.
@app.route('/library', methods=["POST","GET"])
def lib():
    
    url = "http://openlibrary.org/search.json"
    listOBooks = ['CapTain UnderPants', 'animOrphs', 'Game of Thrones', 'Twilight', "cats"]
    book = listOBooks[1].lower()

    querystring = {"q": book}
    response = requests.request("GET", url, params=querystring)
    library = response.json()

    jason = {}
    jason = library['docs']

    new_dict = {}
    def preprocess(my_info):
      i = 0
      while i < 26:
        if 'isbn' in my_info[i]:
          new_dict[i] = my_info[i]
          i += 1
        else:
          i += 1      

      return new_dict  

    preprocess(jason)
    return render_template('library.html', value=new_dict)


#Couldn't get the other two pages to load. I would reccomend running them seperately on powershell.