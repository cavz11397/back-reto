from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infraestructure.db.db import get_db
from app.security.autenticationJWT import createToken
from app.domain.entities.user import User
from app.infraestructure.repositories.loginRepository import LoginRepository
from app.infraestructure.services.loginService import LoginService

router = APIRouter()

@router.post("/login", tags=["login"])
def login(user: User, db: Session = Depends(get_db)):
    repository = LoginRepository(db)
    service = LoginService(repository)
    
    userdb = service.authenticate(user.username, user.password)
    if not userdb:
        raise HTTPException(status_code=403, detail="Invalid username or password")
    return {"token": createToken(user.dict()), "account":userdb.account}