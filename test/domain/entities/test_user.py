import pytest
from app.domain.entities.user import User

def test_user_model():
    user = User(username="test_user", password="test_password")
    assert user.username == "test_user"
    assert user.password == "test_password"