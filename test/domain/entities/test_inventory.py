import pytest
from app.domain.entities.inventory import InventoryDTO

def test_default_id_inventory():
    inventory = InventoryDTO(id_account="test_account", name="test_inventory", description="test_description")
    assert inventory.id_inventory is not None
    assert len(inventory.id_inventory) == 36  # UUID length

def test_name():
    inventory = InventoryDTO(id_account="test_account", name="test_inventory", description="test_description")
    assert inventory.name == "test_inventory"

def test_description():
    inventory = InventoryDTO(id_account="test_account", name="test_inventory", description="test_description")
    assert inventory.description == "test_description"