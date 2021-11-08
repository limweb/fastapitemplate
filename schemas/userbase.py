from typing import List, Optional, Any
import datetime as _dt
from pydantic import  BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserAuth(BaseModel):
    user: User
    access_token: str
    refresh_token: str