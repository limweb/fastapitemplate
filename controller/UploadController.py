from fastapi import APIRouter
from typing import List
import fastapi as _fastapi
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse

import sqlalchemy.orm as _orm
from config.database  import get_db
router = APIRouter(
    prefix="/api/upload",
    tags=['Uploads']
)

@router.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@router.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}


@router.get("/")
async def main():
    content = """
        <body>
        <form action="/api/upload/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/api/upload/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)