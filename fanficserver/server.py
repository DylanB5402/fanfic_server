import flask
from flask import request
import asyncio

try:
    from fanficserver.fanfic_database import FanFicDatabase
except:
    from fanfic_database import FanFicDatabase

fdb = FanFicDatabase()
app = flask.Flask(__name__, static_folder="../static/")

@app.route('/', methods=['GET'])
async def index():
    fic = fdb.get_all_fics()
    return flask.render_template('index.html', fic=fic)

@app.route('/send/', methods = ['POST', 'GET'])   
async def send(): 
    fdb.add_fic(request.form['url'])
    return flask.redirect(flask.url_for('index'))
    
@app.route('/test/', methods = ['GET'])
async def test():
    return "687"
