from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.infraestructure.db.db import get_db
from app.domain.entities.itemInventory import InventoryItemDTO
from app.infraestructure.repositories.itemInventoryRepository import ItemRepository
from app.infraestructure.services.ItemInventoryService import ItemService
from app.interfaces.middlewares.middleware import BearerJWT
from app.config.settings import ITEMS_ROUTES
from app.security.permissions import has_permissions

router = APIRouter()

@router.get(ITEMS_ROUTES['get_by_inventory'], tags=["items"], dependencies=[Depends(BearerJWT())])
def get_all_items(account_id: str = Query(...), id_role: str = Query(...), id_inventory: str = Query(...), db: Session = Depends(get_db)):
    if not has_permissions(db, account_id, id_role, ITEMS_ROUTES['get_by_inventory']):
        raise HTTPException(status_code=403, detail="Permission denied")
    repository = ItemRepository(db)
    service = ItemService(repository)
    items = service.get_all_items_by_inventory(id_inventory)
    if not items:
        raise HTTPException(status_code=404, detail="Account not found")
    return items

@router.post(ITEMS_ROUTES['create'], tags=["items"], dependencies=[Depends(BearerJWT())])
def create_items(items: list[InventoryItemDTO], account_id: str = Query(...), id_role: str = Query(...), db: Session = Depends(get_db)):
    if not has_permissions(db, account_id, id_role,ITEMS_ROUTES['create']):
        raise HTTPException(status_code=403, detail="Permission denied")
    repository = ItemRepository(db)
    service = ItemService(repository)
    return service.create_items(items)