from typing import Optional
from app.domain.entities.login import LoginDTO
from app.domain.usecases.repositories.loginRepositories import LoginRepository

class AuthenticateUserUseCase:
    def __init__(self, login_repository: LoginRepository):
        self.login_repository = login_repository

    def authenticate(self, username: str, password: str) -> Optional[LoginDTO]:
        user = self.login_repository.find_by_username(username)
        if user and user.password == password:
            return user
        return None