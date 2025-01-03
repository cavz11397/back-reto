from dataclasses import dataclass

@dataclass
class LoginDTO:
    id: int
    username: str
    password: str