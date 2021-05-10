from flask import Flask, render_template, url_for
from flask import request
from flask_bootstrap import Bootstrap
import requests, json
from pprint import pprint



app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/display')
def display():
    return render_template('display.html')

@app.route('/library')
def lib():
    return render_template('library.html')    