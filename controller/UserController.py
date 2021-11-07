from fastapi import APIRouter
from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from services import  UserService, PostService
from config  import database as _dbservice
from schemas import User as _schuser, postbase as _schpost,Post as _post

_dbservice.create_database()

router = APIRouter(
    prefix="/api/users",
    tags=['Users']
)

@router.get("/", response_model=List[_schuser.UserOut])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_dbservice.get_db),
):
    users = UserService.get_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=_schuser.UserOut)
def read_user(user_id: int, db: _orm.Session = _fastapi.Depends(_dbservice.get_db)):
    db_user = UserService.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return db_user


@router.post("/{user_id}/posts/", response_model=_post.PostOut)
def create_post(
    user_id: int,
    post: _schpost.PostCreate,
    db: _orm.Session = _fastapi.Depends(_dbservice.get_db),
):
    db_user = UserService.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this user does not exist"
        )
    return PostService.create_post(db=db, post=post, user_id=user_id)
