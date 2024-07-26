from fastapi import FastAPI
from src.modules.auth.controller.AuthController import authRouter
from src.modules.user.controller.UserController import userRouter
from src.modules.views.controller.ViewController import viewRouter
from src.modules.account.controller import account_router
from src.database.db import create_db_and_tables
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(authRouter,tags=['Authentication route'])
app.include_router(userRouter,tags=['Users route'])
app.include_router(viewRouter,tags=['View'])
app.include_router(account_router,tags=['Account'])

@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
    return "create db"