from typing import List, Optional, Any
import datetime as _dt
from pydantic import  BaseModel


class PostBase(BaseModel):
    title: str
    content: str

class UserBase(BaseModel):
    email: str

class PostCreate(PostBase):
    pass

class UserCreate(UserBase):
    password: str

class Post(PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserOut(UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []

    class Config:
        orm_mode = True

class PostOut(PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime
    owner: User

    class Config:
        orm_mode = True