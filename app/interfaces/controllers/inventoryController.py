from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.infraestructure.db.db import get_db
from app.domain.entities.inventory import InventoryDTO 
from app.infraestructure.repositories.inventoryRepository import InventoryRepository
from app.infraestructure.services.inventoryService import InventoryService
from app.interfaces.middlewares.middleware import BearerJWT
from app.config.settings import INVENTORY_ROUTES
from app.security.permissions import has_permissions

router = APIRouter()

@router.get(INVENTORY_ROUTES['get_by_id'], tags=["inventories"], dependencies=[Depends(BearerJWT())])
def get_inventories_by_account(account_id: str = Query(...), id_role: str = Query(...), db: Session = Depends(get_db)):
    if not has_permissions(db, account_id, id_role, INVENTORY_ROUTES['get_by_id']):
        raise HTTPException(status_code=403, detail="Permission denied")
    repository = InventoryRepository(db)
    service = InventoryService(repository)
    inventories = service.get_inventory_by_id_account(account_id)
    if not inventories:
        raise HTTPException(status_code=404, detail="Account not found")
    return inventories

@router.post(INVENTORY_ROUTES['create'], tags=["inventories"], dependencies=[Depends(BearerJWT())])
def create_inventories(inventories: list[InventoryDTO], account_id: str = Query(...), id_role: str = Query(...), db: Session = Depends(get_db)):
    if not has_permissions(db, account_id, id_role, INVENTORY_ROUTES['create']):
        raise HTTPException(status_code=403, detail="Permission denied")
    repository = InventoryRepository(db)
    service = InventoryService(repository)
    return service.create_inventories(inventories)