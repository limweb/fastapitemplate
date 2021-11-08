from fastapi import APIRouter
from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from services import  PostService
from config import database as _dbservice
from schemas.Post import PostOut
import schemas.postbase as _postbase

_dbservice.create_database()

router = APIRouter(
    prefix="/api/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[PostOut])
def read_posts(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_dbservice.get_db),
):
    posts = PostService.get_posts(db=db, skip=skip, limit=limit)
    return posts


@router.get("/{post_id}", response_model=PostOut)
def read_post(post_id: int, db: _orm.Session = _fastapi.Depends(_dbservice.get_db)):
    post = PostService.get_post(db=db, post_id=post_id)
    if post is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this post does not exist"
        )

    return post


@router.delete("/{post_id}")
def delete_post(post_id: int, db: _orm.Session = _fastapi.Depends(_dbservice.get_db)):
    PostService.delete_post(db=db, post_id=post_id)
    return {"message": f"successfully deleted post with id: {post_id}"}


@router.put("/{post_id}", response_model=_postbase.Post)
def update_post(
    post_id: int,
    post: _postbase.PostCreate,
    db: _orm.Session = _fastapi.Depends(_dbservice.get_db),
):
    return PostService.update_post(db=db, post=post, post_id=post_id)