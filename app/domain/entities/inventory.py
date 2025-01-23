from pydantic import BaseModel, Field
from uuid import uuid4


class InventoryDTO(BaseModel):
    id_inventory: str = Field(default_factory=lambda: str(uuid4()))
    id_account: str
    name: str
    description: str