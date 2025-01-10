from pydantic import BaseModel, Field
from uuid import uuid4


class InventoryItemDTO(BaseModel):
    id_item: str = Field(default_factory=lambda: str(uuid4()))
    id_inventory: str
    name: str
    quantity: int
    price: float