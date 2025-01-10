from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.infraestructure.db.db import Base


class Role(Base):
    __tablename__ = 'role'
    
    id_role = Column(String, primary_key=True)  
    role_user = Column(String, nullable=False)  

    logins = relationship("Login", back_populates="role")
    