from typing import List
import fastapi as _fastapi
from config import database as _dbservice
import controller.UserController as UserController
import controller.PostController as PostController
import controller.AuthController as AuthController

app = _fastapi.FastAPI()

_dbservice.create_database()

@app.on_event("startup")
async def startup():
    print('----------------start up------------------')
    # await db.connect()

@app.on_event("shutdown")
async def shutdown():
    print('----------------shutdown------------------')
    # await db.disconnect()

@app.get("/",tags=["root"])
def index() -> dict:
    return  {"message": "Fast Api Server v0.0.1"}

app.include_router(AuthController.router)
app.include_router(UserController.router)
app.include_router(PostController.router)