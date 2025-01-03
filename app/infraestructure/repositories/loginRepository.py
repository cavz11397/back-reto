from typing import Optional
from sqlalchemy.orm import Session
from app.domain.entities.login import LoginDTO
from app.domain.usecases.repositories.loginRepositories import LoginRepository
from app.infraestructure.db.login import Login

class SQLAlchemyLoginRepository(LoginRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_by_username(self, username: str) -> Optional[LoginDTO]:
        user = self.db_session.query(Login).filter(Login.username == username).first()
        if user:
            return LoginDTO(id=user.id, username=user.username, password=user.password)
        return None