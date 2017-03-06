from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from rebrickable_db.models import Base

#id,version,set_num
#1,1,7922-1
#3,1,3931-1

class Inventory(Base):
    __tablename__='inventories'
    id = Column(Integer,primary_key=True)
    version = Column(Integer)
    set_num = Column(ForeignKey('sets.set_num'))