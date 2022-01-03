from db import db
from models.enums import RoleType


class BaseUsers(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(RoleType), default=RoleType.user, nullable=False)


class UsersModel(BaseUsers):
    __tablename__ = "users"
