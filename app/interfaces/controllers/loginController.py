from fastapi import APIRouter, Depends, HTTPException
from app.infraestructure.repositories.loginRepository import SQLAlchemyLoginRepository
from app.domain.usecases.authenticateUser import AuthenticateUserUseCase
from app.infraestructure.services.loginService import LoginService
from app.infraestructure.db.db import get_db
from app.security.autenticationJWT import createToken
from app.domain.entities.user import User

router = APIRouter()

@router.post("/login2", tags=["login"])
def login(user: User, db=Depends(get_db)):
    login_repository = SQLAlchemyLoginRepository(db)
    use_case = AuthenticateUserUseCase(login_repository)
    service = LoginService(use_case)
    
    userdb = service.authenticate(user.username, user.password)
    if not userdb:
        raise HTTPException(status_code=403, detail="Invalid username or password")
    return {"token": createToken(user.dict())}
