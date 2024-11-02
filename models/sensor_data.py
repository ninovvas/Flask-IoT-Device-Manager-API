from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

# Sensor Data Model
class SensorDataModel(db.Model):
    __tablename__ = 'sensor_data'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    sensor_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
    value: Mapped[float] = mapped_column(db.Float, nullable=False)
    timestamp: Mapped[db.DateTime] = mapped_column(db.DateTime, server_default=db.func.now())

    sensor: Mapped['SensorModel'] = relationship('SensorModel', back_populates='sensor_data')