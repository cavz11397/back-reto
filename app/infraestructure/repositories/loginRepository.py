from sqlalchemy.orm import Session, joinedload
from app.infraestructure.db.login import Login

class LoginRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_username(self, username: str):
        from app.infraestructure.db.accounts import Account 
        from app.infraestructure.db.role import Role
        return self.session.query(Login).filter_by(username=username).options(
            joinedload(Login.account),
            joinedload(Login.role)
        ).first()