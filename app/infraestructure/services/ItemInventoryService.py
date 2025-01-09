from app.infraestructure.repositories.itemInventoryRepository import ItemRepository
from app.infraestructure.db.itemInventory import InventoryItem

class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def get_all_items(self):
        return self.repository.get_all_items()

    def get_item_by_id(self, item_id: str):
        return self.repository.get_item_by_id(item_id)

    def create_item(self, id_item: str, id_inventory: str, name: str, quantity: int, price: float):
        item = InventoryItem(
            id_item=id_item,
            id_inventory=id_inventory,
            name=name,
            quantity=quantity,
            price=price
        )
        self.repository.add_item(item)
        return item

    # def update_item(self, item_id: str, **kwargs):
    #     return self.repository.update_item(item_id, **kwargs)

    def delete_item(self, item_id: str):
        return self.repository.delete_item(item_id)