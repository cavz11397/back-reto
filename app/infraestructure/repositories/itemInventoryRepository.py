from sqlalchemy.orm import Session
from app.infraestructure.db.itemInventory import InventoryItem

class ItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_items(self):
        return self.session.query(InventoryItem).all()

    def get_item_by_id(self, item_id: str):
        return self.session.query(InventoryItem).filter_by(id_item=item_id).first()

    def add_item(self, item: InventoryItem):
        self.session.add(item)
        self.session.commit()

    def update_item(self, item_id: str, **kwargs):
        item = self.get_item_by_id(item_id)
        if item:
            for key, value in kwargs.items():
                setattr(item, key, value)
            self.session.commit()
        return item

    def delete_item(self, item_id: str):
        item = self.get_item_by_id(item_id)
        if item:
            self.session.delete(item)
            self.session.commit()
        return item