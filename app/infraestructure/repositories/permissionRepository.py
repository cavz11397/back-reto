from sqlalchemy.orm import Session
from app.infraestructure.db.permission import Permission

class PermissionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_permission_by_id_account_role_endpoint(self, id_account: str, id_role: str, endpoint: str):
        return self.session.query(Permission).filter(
            Permission.id_account == id_account,
            Permission.id_role == id_role,
            Permission.endpoint == endpoint
        ).first()