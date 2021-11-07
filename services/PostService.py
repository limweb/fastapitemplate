import sqlalchemy.orm as _orm
from models import Post as _post
from schemas import postbase as postbase

def get_posts(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_post.Post).offset(skip).limit(limit).all()


def create_post(db: _orm.Session, post: postbase.PostCreate, user_id: int):
    post = _post.Post(**post.dict(), owner_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_post(db: _orm.Session, post_id: int):
    return db.query(_post.Post).filter(_post.Post.id == post_id).first()


def delete_post(db: _orm.Session, post_id: int):
    db.query(_post.Post).filter(_post.Post.id == post_id).delete()
    db.commit()


def update_post(db: _orm.Session, post_id: int, post: postbase.PostCreate):
    db_post = get_post(db=db, post_id=post_id)
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post