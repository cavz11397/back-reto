from sqlalchemy.orm import Session
from app.infraestructure.db.inventory import Inventory
from app.domain.entities.inventory import InventoryDTO

class InventoryRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_inventory_by_id_account(self, id_account: str):
        return self.session.query(Inventory).filter(Inventory.id_account == id_account).all()

    def add_inventory(self, inventory_dto: InventoryDTO):
        inventory = Inventory(
            id_inventory=inventory_dto.id_inventory,
            id_account=inventory_dto.id_account,
            name=inventory_dto.name,
            description=inventory_dto.description
        )
        self.session.add(inventory)
        self.session.commit()