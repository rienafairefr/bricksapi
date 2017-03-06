
#part_num,name,part_cat_id
#0687b1,Set 0687 Activity Booklet 1,17
#0901,Baseplate 16 x 30 with Set 080 Yellow House Print,1
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rebrickable_db.models import Base


class Part(Base):
    __tablename__='parts'
    part_num = Column(String,primary_key=True)
    name = Column(String)
    part_cat_id = Column(ForeignKey('partcategories.id'))
    part_cat = relationship('PartCategory')