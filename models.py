from datetime import datetime

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/test.db'
db = SQLAlchemy(app)


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(140))
    body = db.Column(db.String(280))
    author = db.Column(db.String(50))
    dt = db.Column(db.DateTime)

    def __init__(self, link, body, author, dt=None):
        self.link = link
        self.body = body
        self.author = author
        if dt is None:
            self.dt = datetime.utcnow()

    def __repr__(self):
        return '<Link %r>' % self.link[:15]