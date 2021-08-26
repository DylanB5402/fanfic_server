import flask
from flask import request
import asyncio

from fanficserver import downloader
from rq import Queue
# from worker import conn

try:
    from fanficserver.fanfic_database import FanFicDatabase
    from fanficserver.worker import conn
except:
    from worker import conn
    from fanfic_database import FanFicDatabase

fdb = FanFicDatabase()
print('bruh')

app = flask.Flask(__name__, static_folder="../static/")
q = Queue(connection=conn)


@app.route('/', methods=['GET'])
async def index():
    fic = fdb.get_all_fics()
    return flask.render_template('index.html', fic=fic)

@app.route('/send/', methods = ['POST', 'GET'])   
async def send(): 
    fdb.add_fic(request.form['url'])
    # return str(request.form['url'])
    return flask.redirect(flask.url_for('index'))
    
def taco(num):
    # print(num, 687)
    # fdb.test(num)
    fdb.add_fic('cheese')

@app.route('/test/', methods = ['GET'])
async def test():
    # socket.send_string("taco " + "helloWorld!")
    # q.enqueue(taco, 12)
    q.enqueue(taco, 12)
    return "687"
