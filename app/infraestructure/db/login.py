from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.infraestructure.db.db import Base


class Login(Base):
    __tablename__= 'login'
    id = Column(Integer, primary_key=True)
    id_account = Column(String, ForeignKey('accounts.id_account'), nullable=False)  
    username = Column(String)
    password = Column(String)

    account = relationship("Account",back_populates="logins")

    def verify_password(self, password: str) -> bool:
        return self.password == password
