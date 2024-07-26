from src.modules.user.repository.UserRepository import UserRepository
from src.database.db import SessionLocal
from src.modules.user.scheme.UserScheme import CreateUser

class UserService():
    def __init__(self):
      self.userRepository = UserRepository(SessionLocal)

    async def get_all_user(self):
        return await self.userRepository.get_all_user()
      
    async def create_user(self, user:CreateUser):
        return await self.userRepository.create_user(user)