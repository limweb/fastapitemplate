from typing import List, Optional, Any
from schemas import userbase as _userbase
from schemas import postbase as _postbase

class UserOut(_userbase.UserBase):
    id: int
    is_active: bool
    posts: List[_postbase.Post] = []

    class Config:
        orm_mode = True
