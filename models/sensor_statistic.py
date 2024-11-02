from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

# Sensor Statistic Model
class SensorStatisticModel(db.Model):
    __tablename__ = 'sensor_statistic'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    sensor_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('sensor.id'), nullable=False)
    average_value: Mapped[float] = mapped_column(db.Float, nullable=False)
    min_value: Mapped[float] = mapped_column(db.Float, nullable=False)
    max_value: Mapped[float] = mapped_column(db.Float, nullable=False)
    timestamp: Mapped[db.DateTime] = mapped_column(db.DateTime, server_default=db.func.now())

    sensor: Mapped['SensorModel'] = relationship('Sensor', back_populates='sensor_statistics')