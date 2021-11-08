from typing import List, Optional, Any
import datetime as _dt
from schemas import postbase  as _basepost
from schemas.userbase import User

class PostOut(_basepost.PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime
    owner: User

    class Config:
        orm_mode = True