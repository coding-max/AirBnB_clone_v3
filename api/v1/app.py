#!/usr/bin/python3
''' app module '''

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def flask_isnt_fun(chester):
    ''' handles teardown_appcontext '''
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    if (host is None):
        host = '0.0.0.0'
    port = getenv("HBNB_API_PORT")
    if (port is None):
        port = '5000'
    app.run(host, port, threaded=True)

