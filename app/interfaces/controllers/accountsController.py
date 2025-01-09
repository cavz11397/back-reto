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

@router.get(ACCOUNTS_ROUTES['get_all'], tags=["accounts"], dependencies=[Depends(BearerJWT())])
def get_all_accounts(db: Session = Depends(get_db)):
    repository = AccountRepository(db)
    service = AccountService(repository)
    return service.get_all_accounts()

@router.get(ACCOUNTS_ROUTES['get_by_id'], tags=["accounts"], dependencies=[Depends(BearerJWT())])
def get_account_by_id(account_id: str = Query(...), db: Session = Depends(get_db)):
    if not has_permissions(db, account_id, ACCOUNTS_ROUTES['get_by_id']):
        raise HTTPException(status_code=403, detail="Permission denied")
    repository = AccountRepository(db)
    service = AccountService(repository)
    account = service.get_account_by_id(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

# @router.post("/accounts", tags=["accounts"])
# def create_account(account: Account, db: Session = Depends(get_db)):
#     repository = AccountRepository(db)
#     service = AccountService(repository)
#     return service.create_account(
#         id_account=account.id_account,
#         owner_inventory=account.owner_inventory,
#         role_user=account.role_user
#     )

# @router.put("/accounts/{account_id}", tags=["accounts"])
# def update_account(account_id: str, account: Account, db: Session = Depends(get_db)):
#     repository = AccountRepository(db)
#     service = AccountService(repository)
#     updated_account = service.update_account(
#         account_id,
#         owner_inventory=account.owner_inventory,
#         role_user=account.role_user
#     )
#     if not updated_account:
#         raise HTTPException(status_code=404, detail="Account not found")
#     return updated_account

# @router.delete("/accounts/{account_id}", tags=["accounts"])
# def delete_account(account_id: str, db: Session = Depends(get_db)):
#     repository = AccountRepository(db)
#     service = AccountService(repository)
#     deleted_account = service.delete_account(account_id)
#     if not deleted_account:
#         raise HTTPException(status_code=404, detail="Account not found")
#     return {"detail": "Account deleted successfully"}