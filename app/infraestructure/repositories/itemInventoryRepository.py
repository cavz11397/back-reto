from sqlalchemy.orm import Session
from app.infraestructure.db.itemInventory import InventoryItem
from app.domain.entities.itemInventory import InventoryItemDTO

class ItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_items_by_inventory(self, id_inventory: str):
        return self.session.query(InventoryItem).filter(InventoryItem.id_inventory == id_inventory).all()

    def get_item_by_id(self, item_id: str):
        return self.session.query(InventoryItem).filter_by(id_item=item_id).first()

    def add_item(self, item_dto: InventoryItemDTO):
        item = Item(
            id_item=item_dto.id_item,
            id_inventory=item_dto.id_inventory,
            name=item_dto.name,
            quantity=item_dto.quantity,
            price=item_dto.price
        )
        self.session.add(item)
        self.session.commit()