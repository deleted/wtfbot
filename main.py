#!/usr/bin/env python
from wtfbot import app, db

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
