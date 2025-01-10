from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.infraestructure.db.db import Base


class Account(Base):
    __tablename__ = 'accounts'
    
    id_account = Column(String, primary_key=True)  
    owner_inventory = Column(String, nullable=False)  

    logins = relationship("Login",back_populates="account")