from fastapi import APIRouter, Body,Depends
from src.modules.auth.service.AuthService import get_user_disabled_current, get_user_current
from src.modules.user.scheme.UserScheme import CreateUser, User
from src.modules.user.repository.UserRepository import UserRepository
from src.modules.user.service.UserService import UserService


userRouter = APIRouter()

userService = UserService()

@userRouter.get("/users/me")
def user(user: User = Depends(get_user_disabled_current)):
    return user

@userRouter.get("/users")
async def users():
    return await userService.get_all_user()

@userRouter.post("/users", status_code=201)
async def create_user(user_data: CreateUser=Body(...) ):
    return await userService.create_user(user_data)
