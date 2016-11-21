from wtfbot import db
from datetime import datetime


# class Comment(db.Model):
#     comment_id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.Text, nullable=False)
#     timestamp = db.Column(db.DateTime, nullable=False)
#
#     def __init__(self, text, timestamp):
#         self.text = text
#         self.timestamp = timestamp


class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    definitions = db.relationship('Definition', backref='term', lazy='select')

    def __init__(self, text):
        self.text = text


class Definition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term_id = db.Column(db.Integer, db.ForeignKey('term.id'))
    text = db.Column(db.Text, nullable=False)
    example = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    modified_at = db.Column(
        db.DateTime, nullable=False,
        default=datetime.now, onupdate=datetime.now
    )

    def __init__(self, term, text, example=None):
        self.term = term
        self.text = text
        self.example = example
