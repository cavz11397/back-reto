from sqlalchemy.orm import Session
from app.infraestructure.db.accounts import Account
from app.domain.entities.accounts import AccountDTO

class AccountRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_account_by_id(self, account_id: str):
        return self.session.query(Account).filter_by(id_account=account_id).first()

    def add_account(self, account_dto: AccountDTO):
        account = Account(
            id_account=account_dto.id_account,
            owner_inventory=account_dto.owner_inventory,
        )
        self.session.add(account)
        self.session.commit()