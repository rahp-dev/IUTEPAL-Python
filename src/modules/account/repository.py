from sqlalchemy.orm import Session
from src.database.models import Transactions

from sqlalchemy.future import select
class AccountRepository:
    def __init__(self, session: Session):
        self.session = session

    async def add_transaction(self, transactionType:str, amount:float, description:str):
      transaction_data = Transactions(amount = amount,transactionType = transactionType, description=description)
      print(transaction_data)
      async with self.session() as session:
            session.add(transaction_data)
            await session.commit()
            await session.refresh(transaction_data)
      return transaction_data

    async def get_all_transactions(self):
        async with self.session() as session:
            result = await session.execute(select(Transactions))
            transactions = result.scalars().all()
            return transactions

    def get_total_amount(self):
        return sum(t['amount'] for t in self.transactions)
