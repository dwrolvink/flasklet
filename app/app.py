from flask import Flask, request, jsonify, render_template, send_file
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
api = Api(app)

# One page website
# -------------------------------------------------------------
@app.route('/')
def render_homepage():
    return render_template('main/index.html') 

@app.route('/favicon.ico')
def render_favicon():
    return send_file('static/fav.png', mimetype='image/png')

# Simple API
# -------------------------------------------------------------
class getBackgroundColor(Resource):
    def get(self):
        return jsonify({"bg_color": "#2AABF9"}) 

# Add API resources
api.add_resource(getBackgroundColor, '/background_color')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)