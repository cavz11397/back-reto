from app.infraestructure.repositories.permissionRepository import PermissionRepository
from app.infraestructure.db.permission import Permission

class PermissionService:
    def __init__(self, repository: PermissionRepository):
        self.repository = repository

    def get_all_permissions(self):
        return self.repository.get_all_permissions()

    def get_permission_by_id(self, permission_id: str):
        return self.repository.get_permission_by_id(permission_id)

    def get_permission_by_id_account_endpoint(self, id_account: str, endpoint: str):
        return self.repository.get_permission_by_id_account_endpoint(id_account, endpoint)


    # def create_permission(self, id: str, permission: bool, endpoint: str, description: str, id_account: str):
    #     permission = Permission(
    #         id=id,
    #         permission=permission,
    #         endpoint=endpoint,
    #         description=description,
    #         id_account=id_account
    #     )
    #     self.repository.add_permission(permission)
    #     return permission

    # def update_permission(self, permission_id: str, **kwargs):
    #     return self.repository.update_permission(permission_id, **kwargs)

    # def delete_permission(self, permission_id: str):
    #     return self.repository.delete_permission(permission_id)