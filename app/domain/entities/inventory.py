from dataclasses import dataclass


@dataclass
class InventoryDTO:
    id_inventory: str
    id_account: str
    name: str
    description: str