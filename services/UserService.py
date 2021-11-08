import sqlalchemy.orm as _orm
from models import User as _user
from schemas import userbase as _baseuser
from utils.jwt import JWTAUTH
import sys
auth_handler = JWTAUTH()

def get_user(db: _orm.Session, user_id: int):
    return db.query(_user.User).filter(_user.User.id == user_id).first()

def get_user_by_email(db: _orm.Session, email: str):
    return db.query(_user.User).filter(_user.User.email == email).first()


def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_user.User).offset(skip).limit(limit).all()


def create_user(db: _orm.Session, user: _baseuser.UserCreate):
        hashed_passwordx = auth_handler.encode_password(user.password)
        db_user = _user.User(email=user.email, hashed_password=hashed_passwordx)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user