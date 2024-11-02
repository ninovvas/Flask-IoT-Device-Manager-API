from marshmallow import fields

from schemas.base import BaseSensor


# Sensor Schema
class SensorResponseSchema(BaseSensor):
    id = fields.Integer(required=True)
    room_id = fields.Integer(required=True)
