import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infraestructure.db.accounts import Account, Base
from app.infraestructure.db.login import Login
from app.infraestructure.db.role import Role

# Configuración de la base de datos en memoria para pruebas
DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    # Crear las tablas en la base de datos en memoria
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_account(db):
    # Limpiar la base de datos antes de la prueba
    db.query(Login).delete()
    db.query(Account).delete()
    db.query(Role).delete()
    db.commit()

    # Crear una cuenta de prueba
    account = Account(id_account="123", owner_inventory="inventory1")
    db.add(account)
    db.commit()

    # Verificar que la cuenta se haya creado correctamente
    result = db.query(Account).filter_by(id_account="123").first()
    assert result is not None
    assert result.id_account == "123"
    assert result.owner_inventory == "inventory1"

def test_account_relationship_with_login(db):
    # Limpiar la base de datos antes de la prueba
    db.query(Login).delete()
    db.query(Account).delete()
    db.query(Role).delete()
    db.commit()

    # Crear una cuenta de prueba
    account = Account(id_account="123", owner_inventory="inventory1")
    db.add(account)
    db.commit()

    # Crear un rol de prueba
    role = Role(id_role="789", role_user="admin")
    db.add(role)
    db.commit()

    # Crear un login asociado a la cuenta y al rol
    login = Login(id="456", username="test_user", password="test_password", id_account="123", id_role="789")
    db.add(login)
    db.commit()

    # Verificar la relación entre Account y Login
    result = db.query(Account).filter_by(id_account="123").first()
    assert result is not None
    assert len(result.logins) == 1
    assert result.logins[0].username == "test_user"
    assert result.logins[0].role.role_user == "admin"