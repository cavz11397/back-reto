from app.infraestructure.repositories.inventoryRepository import InventoryRepository
from app.infraestructure.db.inventory import Inventory
from app.domain.entities.inventory import InventoryDTO


class InventoryService:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def get_inventory_by_id_account(self, id_account: str):
        return self.repository.get_inventory_by_id_account(id_account)

    def create_inventories(self, inventories: list[InventoryDTO]):
        for inventory in inventories:
            self.repository.add_inventory(inventory)
        return {"detail": "Inventories created successfully"}