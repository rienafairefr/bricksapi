
# set_num,name,year,theme_id,num_parts
# 00-1,Weetabix Castle,1970,414,471
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rebrickable_db.models import Base


class Set(Base):
    __tablename__ = 'sets'
    set_num = Column(String, primary_key=True)
    name= Column(String)
    year = Column(Integer)
    theme_id = Column(ForeignKey('themes.id'))
    theme = relationship('Theme')
    num_parts = Column(String)
