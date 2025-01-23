import pytest
from app.domain.entities.login import LoginDTO

def test_login_dto():
    login = LoginDTO(id=1, username="test_user", password="test_password")
    assert login.id == 1
    assert login.username == "test_user"
    assert login.password == "test_password"