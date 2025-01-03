from typing import Optional
from app.domain.entities.login import LoginDTO
from app.domain.usecases.authenticateUser import AuthenticateUserUseCase

class LoginService:
    def __init__(self, authenticate_user_use_case: AuthenticateUserUseCase):
        self.authenticate_user_use_case = authenticate_user_use_case

    def authenticate(self, username: str, password: str) -> Optional[LoginDTO]:
        return self.authenticate_user_use_case.authenticate(username, password)
