from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from config import database as _dbservice
# from  controller import UserController as user_ctl, PostController as post_ctl
from  controller import UserController as user_ctl , PostController as post_ctl

app = _fastapi.FastAPI()

_dbservice.create_database()

@app.get("/")
def index():
    return  {"message": "Fast Api Server v0.0.1"}

app.include_router(user_ctl.router)
app.include_router(post_ctl.router)