from app.infraestructure.repositories.itemInventoryRepository import ItemRepository
from app.infraestructure.db.itemInventory import InventoryItem
from app.domain.entities.itemInventory import InventoryItemDTO


class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def get_all_items_by_inventory(self, id_inventory: str):
        return self.repository.get_all_items_by_inventory(id_inventory)

    def get_item_by_id(self, item_id: str):
        return self.repository.get_item_by_id(item_id)

    def create_items(self, items: list[InventoryItemDTO]):
        for item in items:
            self.repository.add_item(item)
        return {"detail": "Items created successfully"}