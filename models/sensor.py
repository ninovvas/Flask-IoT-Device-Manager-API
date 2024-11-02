from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

# Sensor Model
class SensorModel(db.Model):
    __tablename__ = 'sensor'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    sensor_type: Mapped[str] = mapped_column(db.String(100), nullable=False)
    producer: Mapped[str] = mapped_column(db.String(150), nullable=False)
    interface: Mapped[str] = mapped_column(db.String(150), nullable=False)
    room_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('room.id'), nullable=True)

    room: Mapped['RoomModel'] = relationship('Room', back_populates='sensors', lazy='joined')
    sensor_data: Mapped[list['SensorDataModel']] = relationship('SensorDataModel', back_populates='sensor',
            lazy=True)
    sensor_schedules: Mapped[list['SensorScheduleModel']] = relationship('SensorScheduleModel',
            back_populates='sensor', lazy=True)
    sensor_statistics: Mapped[list['SensorStatisticModel']] = relationship('SensorStatisticModel',
            back_populates='sensor',lazy=True)