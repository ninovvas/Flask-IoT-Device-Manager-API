from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models import UserModel
from models.enums import RoleType

# Home Model
class HomeModel(db.Model):
    __tablename__ = 'home'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)

    address: Mapped[str] = mapped_column(db.String(255), nullable=False)
    city: Mapped[str] = mapped_column(db.String(100), nullable=False)
    state: Mapped[str] = mapped_column(db.String(100), nullable=False)
    zip_code: Mapped[str] = mapped_column(db.String(20), nullable=False)

    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner: Mapped['UserModel'] = relationship('UserModel', back_populates='homes')

    # Timestamp columns to keep track of creation and modification
    created_at: Mapped[db.DateTime] = mapped_column(db.DateTime, server_default=db.func.now())
    updated_at: Mapped[db.DateTime] = mapped_column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())