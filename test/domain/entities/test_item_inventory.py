import pytest
from app.domain.entities.itemInventory import InventoryItemDTO

def test_default_id_item():
    item = InventoryItemDTO(id_inventory="test_inventory", name="test_item", quantity=10, price=99.99)
    assert item.id_item is not None
    assert len(item.id_item) == 36  # UUID length

def test_id_inventory():
    item = InventoryItemDTO(id_inventory="test_inventory", name="test_item", quantity=10, price=99.99)
    assert item.id_inventory == "test_inventory"

def test_name():
    item = InventoryItemDTO(id_inventory="test_inventory", name="test_item", quantity=10, price=99.99)
    assert item.name == "test_item"

def test_quantity():
    item = InventoryItemDTO(id_inventory="test_inventory", name="test_item", quantity=10, price=99.99)
    assert item.quantity == 10

def test_price():
    item = InventoryItemDTO(id_inventory="test_inventory", name="test_item", quantity=10, price=99.99)
    assert abs(item.price - 99.99) < 1e-9