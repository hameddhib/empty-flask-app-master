# -*- coding: utf-8 -*-

from flask import Flask
from flask import json
from flask import Response
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from .user.user import user
app.register_blueprint(user)


@app.errorhandler(404)
def not_found(error):
    response = Response(
        response=json.dumps({"data":"page not found"}),
        status=400,
        mimetype='application/json'
    )
    return response


@app.errorhandler(500)
def server_error(error):
    response = Response(
        response=json.dumps({"data":"page not found"}),
        status=500,
        mimetype='application/json'
    )
    return response
