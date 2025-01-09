from app.infraestructure.repositories.inventoryRepository import InventoryRepository
from app.infraestructure.db.inventory import Inventory

class InventoryService:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def get_all_inventories(self):
        return self.repository.get_all_inventories()

    # def get_inventory_by_id(self, inventory_id: str):
    #     return self.repository.get_inventory_by_id(inventory_id)

    # def create_inventory(self, id_inventory: str, name: str, description: str, quantity: int):
    #     inventory = Inventory(
    #         id_inventory=id_inventory,
    #         name=name,
    #         description=description,
    #         quantity=quantity
    #     )
    #     self.repository.add_inventory(inventory)
    #     return inventory

    # def update_inventory(self, inventory_id: str, **kwargs):
    #     return self.repository.update_inventory(inventory_id, **kwargs)

    # def delete_inventory(self, inventory_id: str):
    #     return self.repository.delete_inventory(inventory_id)