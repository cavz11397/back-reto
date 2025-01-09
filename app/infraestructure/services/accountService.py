from app.infraestructure.repositories.accountRepository import AccountRepository
from app.infraestructure.db.accounts import Account

class AccountService:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def get_all_accounts(self):
        return self.repository.get_all_accounts()

    def get_account_by_id(self, account_id: str):
        return self.repository.get_account_by_id(account_id)

    # def create_account(self, id_account: str, owner_inventory: str, role_user: str):
    #     account = Account(
    #         id_account=id_account,
    #         owner_inventory=owner_inventory,
    #         role_user=role_user
    #     )
    #     self.repository.add_account(account)
    #     return account

    # def update_account(self, account_id: str, **kwargs):
    #     return self.repository.update_account(account_id, **kwargs)

    # def delete_account(self, account_id: str):
    #     return self.repository.delete_account(account_id)