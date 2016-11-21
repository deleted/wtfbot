from flask import render_template, url_for, redirect
from wtfbot import app, db
from models import Term, Definition
import datetime

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
