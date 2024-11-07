from marshmallow import fields

from schemas.base import BaseSensorData


# Sensor Schema
class SensorDataResponseSchema(BaseSensorData):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    timestamp = fields.DateTime(required=True)
