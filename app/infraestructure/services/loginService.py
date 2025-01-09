from app.infraestructure.repositories.loginRepository import LoginRepository

class LoginService:
    def __init__(self, repository: LoginRepository):
        self.repository = repository

    def authenticate(self, username: str, password: str):
        user = self.repository.get_user_by_username(username)
        if user and user.verify_password(password):
            return user
        return None