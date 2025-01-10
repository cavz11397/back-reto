from app.infraestructure.repositories.permissionRepository import PermissionRepository
from app.infraestructure.db.permission import Permission

class PermissionService:
    def __init__(self, repository: PermissionRepository):
        self.repository = repository

    def get_permission_by_id_account_role_endpoint(self, id_account: str, id_role: str, endpoint: str):
        return self.repository.get_permission_by_id_account_role_endpoint(id_account, id_role, endpoint)