from sqlalchemy.orm import Session
from app.infraestructure.db.inventory import Inventory

class InventoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_inventories(self):
        return self.session.query(Inventory).all()

    # def get_inventory_by_id(self, inventory_id: str):
    #     return self.session.query(Inventory).filter_by(id_inventory=inventory_id).first()

    # def add_inventory(self, inventory: Inventory):
    #     self.session.add(inventory)
    #     self.session.commit()

    # def update_inventory(self, inventory_id: str, **kwargs):
    #     inventory = self.get_inventory_by_id(inventory_id)
    #     if inventory:
    #         for key, value in kwargs.items():
    #             setattr(inventory, key, value)
    #         self.session.commit()
    #     return inventory

    # def delete_inventory(self, inventory_id: str):
    #     inventory = self.get_inventory_by_id(inventory_id)
    #     if inventory:
    #         self.session.delete(inventory)
    #         self.session.commit()
    #     return inventory