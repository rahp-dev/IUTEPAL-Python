from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    id: int
    username: str
    full_name: Union[str,None] = None
    email: Union[str,None] = None
    disabled: Union[bool,None] = None
    class Config:
        from_attributes = True
class UserInDB(User):
    hashed_password: str
    class Config:
        from_attributes = True
        
class CreateUser(BaseModel):
    username: str
    password: str
    full_name: Union[str,None] = None
    email: Union[str,None] = None
    disabled: Union[bool,None] = None
    class Config:
        from_attributes = True 