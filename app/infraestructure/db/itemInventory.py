from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.infraestructure.db.db import Base


class InventoryItem(Base):
    __tablename__ = 'inventory_items'
    
    id_item = Column(String, primary_key=True)  
    id_inventory = Column(String, ForeignKey('inventory.id_inventory'), nullable=False) 
    name = Column(String, nullable=False) 
    quantity = Column(Integer, nullable=False)  
    price = Column(Float, nullable=False)  