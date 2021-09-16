#!/usr/bin/python3
''' Index module '''

from flask import Flask, Blueprint, jsonify
from api.v1.views import app_views


@app_views.route('/status')
def json_returned():
    ''' Returns a Json '''
    return jsonify(status="OK")
