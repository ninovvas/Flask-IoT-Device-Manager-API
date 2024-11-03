from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func

from db import db

# Sensor Data Model
class SensorDataModel(db.Model):
    __tablename__ = 'sensor_data'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    sensor_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
    value: Mapped[float] = mapped_column(db.Float, nullable=False)
    timestamp: Mapped[db.DateTime] = mapped_column(db.DateTime, server_default=func.now())
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    sensor: Mapped['SensorModel'] = relationship('SensorModel', back_populates='sensor_data')