from flask import Flask, render_template, url_for
from flask import request
from flask_bootstrap import Bootstrap
import requests, json
from pprint import pprint


app = Flask(__name__)
bootstrap = Bootstrap(app)


url = "http://openlibrary.org/search.json"


querystring = {"q":"Animorphs"}
response = requests.request("GET", url, params=querystring)
library = response.json()

value = {}
value = library['docs']



@app.route('/library')
def lib():
    return render_template('library.html', value=value)



