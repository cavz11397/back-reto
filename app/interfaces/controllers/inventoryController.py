from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infraestructure.db.db import get_db
from app.domain.entities.inventory import InventoryDTO 
from app.infraestructure.repositories.inventoryRepository import InventoryRepository
from app.infraestructure.services.inventoryService import InventoryService
from app.interfaces.middlewares.middleware import BearerJWT
from app.config.settings import INVENTORY_ROUTES

router = APIRouter()

@router.get(INVENTORY_ROUTES['get_all'], tags=["inventories"], dependencies=[Depends(BearerJWT())])
def get_all_inventories(db: Session = Depends(get_db)):
    repository = InventoryRepository(db)
    service = InventoryService(repository)
    return service.get_all_inventories()

# @router.get("/inventories/{inventory_id}", tags=["inventories"])
# def get_inventory_by_id(inventory_id: str, db: Session = Depends(get_db)):
#     repository = InventoryRepository(db)
#     service = InventoryService(repository)
#     inventory = service.get_inventory_by_id(inventory_id)
#     if not inventory:
#         raise HTTPException(status_code=404, detail="Inventory not found")
#     return inventory

# @router.post("/inventories", tags=["inventories"])
# def create_inventory(inventory: Inventory, db: Session = Depends(get_db)):
#     repository = InventoryRepository(db)
#     service = InventoryService(repository)
#     return service.create_inventory(
#         id_inventory=inventory.id_inventory,
#         name=inventory.name,
#         description=inventory.description,
#         quantity=inventory.quantity
#     )

# @router.put("/inventories/{inventory_id}", tags=["inventories"])
# def update_inventory(inventory_id: str, inventory: Inventory, db: Session = Depends(get_db)):
#     repository = InventoryRepository(db)
#     service = InventoryService(repository)
#     updated_inventory = service.update_inventory(
#         inventory_id,
#         name=inventory.name,
#         description=inventory.description,
#         quantity=inventory.quantity
#     )
#     if not updated_inventory:
#         raise HTTPException(status_code=404, detail="Inventory not found")
#     return updated_inventory

# @router.delete("/inventories/{inventory_id}", tags=["inventories"])
# def delete_inventory(inventory_id: str, db: Session = Depends(get_db)):
#     repository = InventoryRepository(db)
#     service = InventoryService(repository)
#     deleted_inventory = service.delete_inventory(inventory_id)
#     if not deleted_inventory:
#         raise HTTPException(status_code=404, detail="Inventory not found")
#     return {"detail": "Inventory deleted successfully"}