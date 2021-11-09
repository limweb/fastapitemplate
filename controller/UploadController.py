import os
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import secrets
from fastapi import APIRouter
from typing import List
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse,FileResponse
from config.database  import get_db
from decouple import config

router = APIRouter(
    prefix="/api/upload",
    tags=['Uploads']
)

@router.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@router.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    for file in files:

        extension = file.filename.split(".")[1]
        if extension not in ["jpg","png","jpeg"]:
            return {"message":"File extension not allowed"}

        token_name = secrets.token_urlsafe(16) + "." + extension
        generated_name = config("uploadpath") +"/" + token_name
        file_content = file.file.read()
        with open(generated_name,"wb") as f:
            f.write(file_content)
        print(file.filename)
        file.close()

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


@router.get("/file/{fname}")
def getfile(fname: str = None):
    file_path = config('uploadpath') + "/" + fname
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/jpeg", filename=fname)
    return {"error" : "File not found!"}

