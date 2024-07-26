from sqlalchemy import create_engine, Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta
from config.config import Settings

setting = Settings()


DATABASE_URL = f"postgresql+asyncpg://{setting.USER_DB}:{setting.PASSWORD_DB}@{setting.HOST_DB}:{setting.PORT_DB}/{setting.NAME_DB}"

engine =  create_async_engine(DATABASE_URL,pool_pre_ping=True, 
    pool_recycle=3600)

SessionLocal = sessionmaker(class_=AsyncSession ,autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # type: ignore