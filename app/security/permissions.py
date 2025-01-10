from sqlalchemy.orm import Session
from app.infraestructure.db.permission import Permission
from app.infraestructure.repositories.permissionRepository import PermissionRepository
from app.infraestructure.services.permissionService import PermissionService

def has_permissions(db: Session, account_id: str, id_role: str, endpoint: str):
    repository = PermissionRepository(db)
    service = PermissionService(repository)
    permission = service.get_permission_by_id_account_role_endpoint(account_id, id_role, endpoint)
    if not permission:
        return False
    return permission.permission
