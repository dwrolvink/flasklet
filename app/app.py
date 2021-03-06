from flask import Flask, render_template, send_file, g
from flask_restful import Api
from flask_cors import CORS

# Init app
# -------------------------------------------------------------
app = Flask(__name__)
CORS(app)
api = Api(app)

# Simple website
# -------------------------------------------------------------
@app.route('/')
def render_homepage():
    g.title = 'Flasklet'
    return render_template('main/index.html') 

@app.route('/cat')
def render_page2():
    g.title = 'Flasklet - Cat'
    return render_template('main/cat.html')    

@app.route('/favicon.ico')
def render_favicon():
    return send_file('static/fav.png', mimetype='image/png')

# Simple API
# -------------------------------------------------------------
from app_api import *
api_prefix = '/api/v1'
api.add_resource(getBackgroundColor, api_prefix+'/background_color')

# Run
# -------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)