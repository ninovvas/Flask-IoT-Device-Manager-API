from marshmallow import fields

from schemas.base import BaseSensor
from schemas.response.sensor_data import SensorDataResponseSchema
from schemas.response.sensor_schedule import SensorScheduleResponseSchema
from schemas.response.sensor_statistic import SensorStatisticResponseSchema


# Sensor Schema
class SensorResponseSchema(BaseSensor):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    sensor_data = fields.Nested(SensorDataResponseSchema, many=True)
    sensor_schedules = fields.Nested(SensorScheduleResponseSchema, many=True)
    sensor_statistics = fields.Nested(SensorStatisticResponseSchema, many=True)
