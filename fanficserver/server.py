import flask
from flask import request
import asyncio

from fanficserver import downloader
from rq import Queue

try:
    from fanficserver.fanfic_database import FanFicDatabase
    from fanficserver.sqlite_fic_queue import SQLiteFicQueue
except:
    from fanfic_database import FanFicDatabase
    from sqlite_fic_queue import SQLiteFicQueue

fdb = FanFicDatabase()
app = flask.Flask(__name__, static_folder="../static/")
queue = SQLiteFicQueue()

@app.route('/', methods=['GET'])
async def index():
    fic = fdb.get_all_fics()
    return flask.render_template('index.html', fic=fic)

@app.route('/send/', methods = ['POST', 'GET'])   
async def send(): 
    fdb.add_fic(request.form['url'])
    queue.push(request.form['url'])
    queue.print_db()
    return flask.redirect(flask.url_for('index'))
    
@app.route('/test/', methods = ['GET'])
async def test():
    return "687"
