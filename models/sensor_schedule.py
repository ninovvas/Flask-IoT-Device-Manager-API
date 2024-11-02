from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

# Sensor Schedule Model
class SensorScheduleModel(db.Model):
    __tablename__ = 'sensor_schedule'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    sensor_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('sensor.id'), nullable=True)
    start_time: Mapped[db.DateTime] = mapped_column(db.DateTime, nullable=False)
    end_time: Mapped[db.DateTime] = mapped_column(db.DateTime, nullable=False)
    action: Mapped[str] = mapped_column(db.String(50), nullable=False)

    sensor: Mapped['SensorModel'] = relationship('Sensor', back_populates='schedules', lazy='joined')