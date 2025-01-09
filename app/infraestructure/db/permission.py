from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.infraestructure.db.db import Base


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(String, primary_key=True)  
    permission = Column(Boolean, nullable=False) 
    endpoint = Column(String)  
    description = Column(String)  
    id_account = Column(String, ForeignKey('accounts.id_account'))
