# coding=utf-8
from flask import render_template, url_for, redirect, request
from wtfbot import app, db
from models import Term, Definition
import datetime
import json

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = CommentForm()
#     if form.validate_on_submit():
#         comment = Comment(
#             form.text.data,
#             datetime.datetime.now()
#         )
#         db.session.add(comment)
#         db.session.commit()
#         return redirect(url_for('index'))
#     comments = Comment.query.order_by(db.desc(Comment.timestamp))
#     return render_template('index.html', comments=comments, form=form)

@app.route('/', methods=['GET'])
def index():
    terms = Term.query.order_by(db.asc(Term.text))
    return render_template('index.html', terms=terms)

def find_term(search_qry):
    term = Term.query.filter(Term.text.ilike(search_qry)).first()
    return term


@app.route('/wtf', methods=['POST'])
def wtf():
    '''
    Return a slack response that defines the term.
    '''
    data = request.form
    search = data.get('text')

    term = find_term(search)
    if term:
        definition = term.definitions[-1]

        return json.dumps({
            "response_type": "in_channel",
            "text": term.text,
            "attachments": {
                "text": definition.text
            }

        })
    else:
        return json.dumps({
            "response_type": "in_channel",
            "text": u"¯\_(ツ)_/¯",
            "Attachments": {
                "text": "Click here to define %s" % search
            }
        })
