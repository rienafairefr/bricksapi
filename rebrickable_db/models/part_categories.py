#  id,name
#  1,Baseplates
#  2,Bricks Printed
from sqlalchemy import Column
from sqlalchemy import Integer,String

from rebrickable_db.models import Base


class PartCategory(Base):
    __tablename__='partcategories'
    id = Column(Integer,primary_key=True)
    name = Column(String)