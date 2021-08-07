import flask
from flask import request
import asyncio

from fanficserver import downloader

app = flask.Flask(__name__, static_folder="../static/")

@app.route('/', methods=['GET'])
async def index():
    return flask.send_from_directory('../static/', 'index.html')

@app.route('/send/', methods = ['POST', 'GET'])   
async def send(): 
    
    return str(request.form['url'])
    

