from pydantic import BaseModel, Field
from uuid import uuid4


class AccountDTO(BaseModel):
    id_account: str = Field(default_factory=lambda: str(uuid4()))
    owner_inventory: str