import os
from csv import reader

from db import Session, engine
from rebrickable_db.models import Base
from rebrickable_db.models.colors import Color
from rebrickable_db.models.inventories import Inventory
from rebrickable_db.models.inventory_parts import InventoryPart
from rebrickable_db.models.inventory_sets import InventorySet
from rebrickable_db.models.part_categories import PartCategory
from rebrickable_db.models.parts import Part
from rebrickable_db.models.sets import Set
from rebrickable_db.models.themes import Theme


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
session = Session()

data={
'colors.csv':Color,
'inventories.csv':Inventory,
'inventory_parts.csv':InventoryPart,
'inventory_sets.csv':InventorySet,
'part_categories.csv':PartCategory,
'parts.csv':Part,
'sets.csv':Set,
'themes.csv':Theme,
}


for filename,typ in data.items():
    print('Treating %s ...'%filename)
    csv_reader = reader(open(os.path.join('rebrickable_data', filename),encoding='utf-8'))
    headers = next(csv_reader, None)
    dictionaries=[]
    for row in csv_reader:
        dictionary = {headers[i]:row[i] for i in range(len(headers))}
        dictionaries.append(dictionary)
    session.bulk_insert_mappings(typ,dictionaries)
    session.commit()