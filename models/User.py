import sqlalchemy as _sql
import sqlalchemy.orm as orm
from config.database import Base

class User(Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    hashed_password = _sql.Column(_sql.String)
    is_active = _sql.Column(_sql.Boolean, default=True)

    posts = orm.relationship("Post", back_populates="owner")