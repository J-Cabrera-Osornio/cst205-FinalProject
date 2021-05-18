##Contributor: Jim O. Cabrera
# Team: 26
# CST 205: Multimedia Design
# May 17, 2021 
# Abstract: This part of the app is a library app that connects to the Open Library Search API 
# to display images and information on books. 
# #
from flask import Flask, render_template, url_for
from flask import request
from flask_bootstrap import Bootstrap
import requests, json


app = Flask(__name__)
bootstrap = Bootstrap(app)


#Tried getting post and get from form tags but I would keep getting a keyerror. Also I moved the code
#into the route definition for ease of use.
@app.route('/library', methods=["POST","GET"])
def lib():
    #Api is taken from OpenLibrary.com, specifically the search api.
    url = "http://openlibrary.org/search.json"

    #Here are a small sample of books and words to use through search api.
    listOBooks = ['CapTain UnderPants', 'animOrphs', 'Game of Thrones', 'Twilight', "cats"]
    book = listOBooks[1].lower()

    #querystring = {"q": "Captain Underpants"} #unomment and type in to write string manually
    querystring = {"q": book}
    response = requests.request("GET", url, params=querystring)
    library = response.json()

    jason = {}
    jason = library['docs']
    # def preproccess reused from previous Homework.
    # I struggled a lot trying to figure out how to extract the api information. I initially thoughgt it would be simple
    # since I had done it many time before in other classes but I keep making the same mistake of understimating how tricky
    # it is to extract the information.
    # 
    # At first, I tried to use a for loop and it worked but I struggled to fetch the isbn part of the api. This
    # api is not the cleanest and most organized, most information is organized exactly where it is but other data is 
    # scrambled and unreliable to call on at times. OpenLibrary did state that their api was not stable and
    # thus to make it easier for myself, I used a while loop to filter out results with isbn in the same index
    # to avoid errors. 
    # #
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

    
