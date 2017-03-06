from contextlib import contextmanager

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from rebrickable_db.models import Base
from rebrickable_db.models import *

engine = create_engine('sqlite:///data.db', echo=True)

Base.metadata.create_all(engine)
# create a configured "Session" class
Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

