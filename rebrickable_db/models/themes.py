
# id,name,parent_id
#1,Technic,
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rebrickable_db.models import Base

#id,name,parent_id
#1,Technic,

class Theme(Base):
    __tablename__ = 'themes'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    parent_id = Column(ForeignKey('themes.id'))
    parent = relationship('Theme', remote_side=[id])
