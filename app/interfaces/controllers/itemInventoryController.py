from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.infraestructure.db.db import get_db
from app.domain.entities.itemInventory import InventoryItemDTO
from app.infraestructure.repositories.itemInventoryRepository import ItemRepository
from app.infraestructure.services.ItemInventoryService import ItemService
from app.interfaces.middlewares.middleware import BearerJWT
from app.config.settings import ITEMS_ROUTES

router = APIRouter()

@router.get(ITEMS_ROUTES['get_all'], tags=["items"], dependencies=[Depends(BearerJWT())])
def get_all_items(owner: str = Query(...), role: str = Query(...), db: Session = Depends(get_db)):
    # Verificar permisos
    # if not has_permission(owner_role):
    #     raise HTTPException(status_code=403, detail="Permission denied")
    repository = ItemRepository(db)
    service = ItemService(repository)
    return service.get_all_items()

# @router.get("/items/{item_id}", tags=["items"])
# def get_item_by_id(item_id: str, db: Session = Depends(get_db)):
#     repository = ItemRepository(db)
#     service = ItemService(repository)
#     item = service.get_item_by_id(item_id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item

# @router.post("/items", tags=["items"])
# def create_item(item: InventoryItemDTO, db: Session = Depends(get_db)):
#     repository = ItemRepository(db)
#     service = ItemService(repository)
#     return service.create_item(
#         id_item=item.id_item,
#         id_inventory=item.id_inventory,
#         name=item.name,
#         quantity=item.quantity,
#         price=item.price
#     )

# @router.put("/items/{item_id}", tags=["items"])
# def update_item(item_id: str, item: InventoryItem, db: Session = Depends(get_db)):
#     repository = ItemRepository(db)
#     service = ItemService(repository)
#     updated_item = service.update_item(
#         item_id,
#         id_inventory=item.id_inventory,
#         name=item.name,
#         quantity=item.quantity,
#         price=item.price
#     )
#     if not updated_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return updated_item

# @router.delete("/items/{item_id}", tags=["items"])
# def delete_item(item_id: str, db: Session = Depends(get_db)):
#     repository = ItemRepository(db)
#     service = ItemService(repository)
#     deleted_item = service.delete_item(item_id)
#     if not deleted_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"detail": "Item deleted successfully"}