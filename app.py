import flask
from flask import request

app = flask.Flask(__name__, static_folder="static/")

@app.route('/', methods=['GET'])
def index():
    return flask.send_from_directory('static/', 'index.html')

@app.route('/send/', methods = ['POST', 'GET'])   
def send(): 
    # print(request.form['url'])
    return str(request.form['url'])

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)