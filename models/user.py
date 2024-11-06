from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.enums import RoleType


# User Model
class UserModel(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(200), nullable=False)
    first_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    role: Mapped[RoleType] = mapped_column(db.Enum(RoleType), nullable=False, default=RoleType.user.name)

    homes: Mapped[list['HomeModel']] = relationship('HomeModel', back_populates='owner', lazy=True)