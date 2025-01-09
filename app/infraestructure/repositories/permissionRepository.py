from sqlalchemy.orm import Session
from app.infraestructure.db.permission import Permission

class PermissionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_permissions(self):
        return self.session.query(Permission).all()

    def get_permission_by_id(self, permission_id: str):
        return self.session.query(Permission).filter_by(id=permission_id).first()

    def get_permission_by_id_account_endpoint(self, id_account: str, endpoint: str):
        return self.session.query(Permission).filter(
            Permission.id_account == id_account,
            Permission.endpoint == endpoint
        ).first()

    # def add_permission(self, permission: Permission):
    #     self.session.add(permission)
    #     self.session.commit()

    # def update_permission(self, permission_id: str, **kwargs):
    #     permission = self.get_permission_by_id(permission_id)
    #     if permission:
    #         for key, value in kwargs.items():
    #             setattr(permission, key, value)
    #         self.session.commit()
    #     return permission

    # def delete_permission(self, permission_id: str):
    #     permission = self.get_permission_by_id(permission_id)
    #     if permission:
    #         self.session.delete(permission)
    #         self.session.commit()
    #     return permission