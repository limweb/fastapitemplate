import fastapi as _fastapi
from config import database as _dbservice
import controller.UserController as UserController
import controller.PostController as PostController
import controller.AuthController as AuthController
import controller.UploadController as UploadController
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = _fastapi.FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_dbservice.create_database()

app.mount("/static", StaticFiles(directory="static"), name="static")

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
app.include_router(UploadController.router)