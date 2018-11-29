# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, make_response
from flask import json
from flask import Response
from .model import User

user = Blueprint('user', __name__)

@user.route('/user', methods = ['GET'])
def get():
    users = User.query.all()
    response =  jsonify(users=[i.serialize() for i in users])
    response.status_code = 200
    return response

@user.route('/user/add', methods = ['POST'])
def post():
    response = Response(
        response=json.dumps({"status":200, "data":"get data"}),
        status=200,
        mimetype='application/json'
    )
    return response

@user.route('/user/edit', methods = ['PUT'])
def put():
    response = Response(
        response=json.dumps({"status":200, "data":"put data"}),
        status=200,
        mimetype='application/json'
    )
    return response

@user.route('/user/delete', methods = ['DELETE'])
def delete():
    response = Response(
        response=json.dumps({"status":200, "data":"delete data"}),
        status=200,
        mimetype='application/json'
    )
    return response
