from flask import Flask, render_template, url_for
from flask import request
from flask_bootstrap import Bootstrap
import requests, json
from pprint import pprint
import webbrowser
from bs4 import BeautifulSoup


app = Flask(__name__)
bootstrap = Bootstrap(app)


url = "http://openlibrary.org/search.json"


querystring = {"q":"captainunderpants"}
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



for i in new_dict:
  pprint(new_dict[i]['isbn'][0])

@app.route('/library')
def lib():
    return render_template('library.html', value=new_dict)


@app.route('/display')
def disp():
  return render_template('display.html', value=new_dict)
