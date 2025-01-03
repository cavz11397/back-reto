from sqlalchemy import Column, Integer, String
from app.infraestructure.db.db import Base


class Login(Base):
    __tablename__= 'login'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
