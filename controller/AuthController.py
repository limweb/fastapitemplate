from fastapi import APIRouter
from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from config import database as _dbservice

router = APIRouter(
    prefix="/api/auth",
    tags=['auths']
)

@router.post("/signup")
def sign_up() -> dict:
    return { "msg": "singup" }

@router.post("/signin")
@router.post("/login")
def sign_in():
    return { "msg": "login" }

@router.get("/signout")
@router.get("/logout")
def sign_out():
    return { "msg": "logout" }
