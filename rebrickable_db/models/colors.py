from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from rebrickable_db.models import Base

#id,name,rgb,is_trans
#-1,Unknown,0033B2,f
#0,Black,05131D,f


class Color(Base):
    __tablename__ = 'colors'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    rgb=Column(String)
    is_trans = Column(Boolean)
