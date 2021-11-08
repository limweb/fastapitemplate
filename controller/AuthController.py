from fastapi import APIRouter
from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from config.database import get_db
from fastapi import FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from utils.jwt import JWTAUTH
from utils.jwtpk import JWTAUTHPK

from services import  UserService
import schemas.userbase as _userbase
from schemas.User import UserOut

router = APIRouter(
    prefix="/api/auth",
    tags=['auths']
)


security = HTTPBearer()
# auth_handler = JWTAUTH() # user secert key
auth_handler = JWTAUTHPK() # used  private.key and public.key

@router.post('/signup')
def signup(user_details: _userbase.UserCreate,db: _orm.Session = _fastapi.Depends(get_db)):
    if UserService.get_user_by_email(db,user_details.email) != None:
        return 'Account already exists'
    try:
        return UserService.create_user(db,user_details)
    except:
        error_msg = 'Failed to signup user'
        return error_msg

@router.post("/signin",response_model=_userbase.UserAuth)
@router.post('/login',response_model=_userbase.UserAuth)
def login(user_details: _userbase.UserCreate, db: _orm.Session = _fastapi.Depends(get_db)) -> dict:
    user = UserService.get_user_by_email(db,user_details.email)
    if (user is None):
        return HTTPException(status_code=401, detail='Invalid email')
    if (not auth_handler.verify_password(user_details.password,user.hashed_password)):
        return HTTPException(status_code=401, detail='Invalid password')
    access_token = auth_handler.encode_token(user.email)
    refresh_token = auth_handler.encode_refresh_token(user.email)
    return {'access_token': access_token, 'refresh_token': refresh_token, 'user': user}

@router.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    return auth_handler.refresh_token(refresh_token)

@router.post('/secret')
def secret_data(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if(auth_handler.decode_token(token)):
        return 'Top Secret data only authorized users can access this info'

@router.get('/notsecret')
def not_secret_data():
    return 'Not secret data'

@router.get("/signout")
@router.get("/logout")
def sign_out():
    return { "msg": "logout" }