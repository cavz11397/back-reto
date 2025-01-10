from app.infraestructure.repositories.accountRepository import AccountRepository
from app.infraestructure.db.accounts import Account
from app.domain.entities.accounts import AccountDTO

class AccountService:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def get_account_by_id(self, account_id: str):
        return self.repository.get_account_by_id(account_id)

    def create_accounts(self, accounts: list[AccountDTO]):
        for account in accounts:
            self.repository.add_account(account)
        return {"detail": "Accounts created successfully"}