from sqlalchemy import Column, Integer, String, ForeignKey
from app.infraestructure.db.db import Base


class Inventory(Base):
    __tablename__ = 'inventory'
    
    id_inventory = Column(String, primary_key=True)  
    id_account = Column(String, ForeignKey('accounts.id_account'), nullable=False)  
    name = Column(String, nullable=False)  
    description = Column(String)  