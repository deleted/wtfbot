#!/usr/bin/env python
import json
from wtfbot import db
from wtfbot.models import Term, Definition

ACRONYM_FILE = 'fixtures/acronyms.json'

with open(ACRONYM_FILE) as acrofile:
    acronyms = json.loads(acrofile.read())

for acronym in acronyms['acronyms']:
    name = acronym['acro']
    if len(name) < 1:
        continue
    expansion = acronym.get('expansion', '')
    meaning = acronym.get('meaning', '')
    definition_text = ''
    if len(expansion) > 0:
        definition_text += '%s: ' % expansion
    definition_text += meaning

    term = Term.query.filter_by(text=name).first()
    if not term:
        term = Term(name)
        db.session.add(term)
    definition = Definition(term, definition_text)
    db.session.add(definition)
    db.session.commit()
    print("Added a definition for %s" % name)
