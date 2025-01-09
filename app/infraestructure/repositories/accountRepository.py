from sqlalchemy.orm import Session
from app.infraestructure.db.accounts import Account

class AccountRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_accounts(self):
        return self.session.query(Account).all()

    def get_account_by_id(self, account_id: str):
        return self.session.query(Account).filter_by(id_account=account_id).first()

    # def add_account(self, account: Account):
    #     self.session.add(account)
    #     self.session.commit()

    # def update_account(self, account_id: str, **kwargs):
    #     account = self.get_account_by_id(account_id)
    #     if account:
    #         for key, value in kwargs.items():
    #             setattr(account, key, value)
    #         self.session.commit()
    #     return account

    # def delete_account(self, account_id: str):
    #     account = self.get_account_by_id(account_id)
    #     if account:
    #         self.session.delete(account)
    #         self.session.commit()
    #     return account