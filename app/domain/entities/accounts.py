from dataclasses import dataclass

@dataclass
class AccountDTO:
    id_account: str
    owner_inventory: str
    role_user: str