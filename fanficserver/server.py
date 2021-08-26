import flask
from flask import request
import asyncio
import zmq

from fanficserver import downloader

try:
    from fanficserver.fanfic_database import FanFicDatabase
except:
    from fanfic_database import FanFicDatabase

# context = zmq.Context()
fdb = FanFicDatabase()
print('bruh')

# app = flask.Flask(__name__, static_folder="../static/")
# socket = context.socket(zmq.PUB)
# socket.bind("tcp://127.0.0.1:5555")
# app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
async def index():
    fic = fdb.get_all_fics()
    return flask.render_template('index.html', fic=fic)

@app.route('/send/', methods = ['POST', 'GET'])   
async def send(): 
    fdb.add_fic(request.form['url'])
    # return str(request.form['url'])
    return flask.redirect(flask.url_for('index'))
    
@app.route('/test/', methods = ['GET'])
async def test():
    # socket.send_string("taco " + "helloWorld!")
    return "687"