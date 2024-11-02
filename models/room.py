from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

# Room Model
class RoomModel(db.Model):
    __tablename__ = 'room'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    description: Mapped[str] = mapped_column(db.String(200))

    home_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('home.id'), nullable=False)

    home: Mapped["HomeModel"] = relationship('HomeModel', back_populates='room')

