import pytest
from app.domain.entities.accounts import AccountDTO

def test_default_id_account():
    account = AccountDTO(owner_inventory="test_inventory", role_user="test_role")
    assert account.id_account is not None
    assert len(account.id_account) == 36  # UUID length

def test_owner_inventory():
    account = AccountDTO(owner_inventory="test_inventory", role_user="test_role")
    assert account.owner_inventory == "test_inventory"