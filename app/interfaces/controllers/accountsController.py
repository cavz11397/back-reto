from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.infraestructure.db.db import get_db
from app.domain.entities.accounts import AccountDTO
from app.infraestructure.repositories.accountRepository import AccountRepository
from app.infraestructure.services.accountService import AccountService
from app.interfaces.middlewares.middleware import BearerJWT
from app.config.settings import ACCOUNTS_ROUTES
from app.security.permissions import has_permissions


router = APIRouter()

@router.get(ACCOUNTS_ROUTES['get_by_id'], tags=["accounts"], dependencies=[Depends(BearerJWT())])
def get_account_by_id(account_id: str = Query(...), id_role: str = Query(...), db: Session = Depends(get_db)):
    if not has_permissions(db, account_id, id_role, ACCOUNTS_ROUTES['get_by_id']):
        raise HTTPException(status_code=403, detail="Permission denied")
    repository = AccountRepository(db)
    service = AccountService(repository)
    account = service.get_account_by_id(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.post(ACCOUNTS_ROUTES['create'], tags=["accounts"], dependencies=[Depends(BearerJWT())])
def create_accounts(accounts: list[AccountDTO], account_id: str = Query(...), id_role: str = Query(...), db: Session = Depends(get_db)):
    if not has_permissions(db, account_id, id_role, ACCOUNTS_ROUTES['create']):
        raise HTTPException(status_code=403, detail="Permission denied")
    repository = AccountRepository(db)
    service = AccountService(repository)
    return service.create_accounts(accounts)