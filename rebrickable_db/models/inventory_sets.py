from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from rebrickable_db.models import Base

#inventory_id,set_num,quantity
#35,75911-1,1
#35,75912-1,1


class InventorySet(Base):
    __tablename__='inventorysets'
    id = Column(Integer,primary_key=True)
    inventory_id = Column(ForeignKey('inventories.id'))
    inventory = relationship('Inventory', backref='sets')
    set_num = Column(ForeignKey('sets.set_num'))
    quantity = Column(Integer)
