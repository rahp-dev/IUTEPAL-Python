from sqlalchemy import ForeignKey, Integer, create_engine, Column, String, Boolean,Float
from src.database.db import Base
from sqlalchemy.orm import relationship
# Definición del modelo de datos
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String,unique=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    hashed_password= Column(String)
    disabled = Column(Boolean)
    phone = Column(String)
    

class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    amount = Column(Float)
    transactionType = Column(String)
    description = Column(String)


