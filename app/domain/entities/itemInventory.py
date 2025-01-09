from dataclasses import dataclass


@dataclass
class InventoryItemDTO:
    id_item: str
    id_inventory: str
    name: str
    quantity: int
    price: float