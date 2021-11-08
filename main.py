from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from config import database as _dbservice
import controller.UserController as UserController
import controller.PostController as PostController
import controller.AuthController as AuthController

app = _fastapi.FastAPI()

_dbservice.create_database()

@app.get("/",tags=["root"])
def index() -> dict:
    return  {"message": "Fast Api Server v0.0.1"}

app.include_router(AuthController.router)
app.include_router(UserController.router)
app.include_router(PostController.router)