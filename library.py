from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests, json
from pprint import pprint


app = Flask(__name__)
bootstrap = Bootstrap(app)


url = "http://openlibrary.org/search.json"
isbn_url = "https://openlibrary.org/isbn/9780140328721.json"

querystring = {"q":"animorphs"}
response = requests.request("GET", url, params=querystring)
library = response.json()

#pprint(library['docs'][0]['title'])

mydict = {}

mydict = library['docs'][0]['title']

@app.route('/')
def lib():
    return render_template('library.html', value=mydict)

