from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from rebrickable_db.models import Base

# inventory_id,part_num,color_id,quantity,is_spare
# 1,48379c01,72,1,f


class InventoryPart(Base):
    __tablename__='inventoryparts'
    id = Column(Integer,primary_key=True)
    inventory_id = Column(ForeignKey('inventories.id'))
    inventory = relationship('Inventory',backref='parts')
    part_num = Column(String)
    color_id = Column(ForeignKey('colors.id'))
    color = relationship('Color')
    quantity = Column(Integer)
    is_spare = Column(Boolean)