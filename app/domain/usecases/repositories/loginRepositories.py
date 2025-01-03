from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.login import LoginDTO

class LoginRepository(ABC):
    @abstractmethod
    def find_by_username(self, username: str) -> Optional[LoginDTO]:
        pass