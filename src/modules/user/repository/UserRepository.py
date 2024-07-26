from sqlalchemy.future import select
from sqlalchemy.orm import Session
from src.modules.user.scheme.UserScheme import CreateUser
from src.database.models import User
from passlib.context import CryptContext 

class UserRepository():

    def __init__(self, session:Session):
      self.session = session
      self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
      return  self.pwd_context.hash(password)
    
    
    async def get_all_user(self):
        async with self.session() as session:
            result = await session.execute(select(User))
            users = result.scalars().all()
            return users

    async def create_user(self, user_data):
        hashed_password = self.hash_password(user_data.password)  # No usar await aquí.
        user = User(username= user_data.username, hashed_password=hashed_password,email=user_data.email,disabled=False, full_name=user_data.full_name )
        async with self.session() as session:
              session.add(user)
              await session.commit()
              await session.refresh(user)
              return user_data
