from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy() 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User {0}>'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }