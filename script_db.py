from sqlalchemy import and_

from db import Session
from rebrickable_db.models.themes import Theme


def filter_theme(t):
    return t.parent is not None and t.parent.name == "Harry Potter"


session = Session()
sets=[]
for theme in session.query(Theme).filter(Theme.parent_id!=None).all():
    if filter_theme(theme):
        sets.extend(theme.sets)

pass
