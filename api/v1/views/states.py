#!/usr/bin/python3
''' States manager '''


from os import stat_result
from flask import Flask, Blueprint, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/states', methods=['GET'])
def all_my_states():
    '''Retrieve all states'''
    states = storage.all(State)
    res = []
    for state in states.values():
        res.append(state.to_dict())
    return jsonify(res)


@app_views.route('/states<string:state_id>', methods=['GET'])
def get_state_by_id(id):
    ''' Retrieve a state by it's id '''
    state = storage.get(State, id)
    if state is None:
        abort(404)


@app_views.route('/states/<string:state_id>', methods=['DELETE'])
def delete_state_by_id(id):
    """returns an empty dictionary with the status code 200
       if the <state_id> is not linked to any 'State', raise a 404 error"""
    state = storage.get(State, id)
    if state is None:
        abort(404)
    