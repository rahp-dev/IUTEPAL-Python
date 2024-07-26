from .repository import AccountRepository
from src.database.db import SessionLocal

class AccountService:
    def __init__(self):
        self.repository = AccountRepository(SessionLocal)

    def get_all_transactions(self):
        transactions = self.repository.get_all_transactions()
        return transactions

    async def create_transaction(self,transactionType:str, amount:float, description:str):
      transaction =  await self.repository.add_transaction(transactionType,amount, description)
      return transaction