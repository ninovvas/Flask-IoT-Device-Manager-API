from marshmallow import fields
from schemas.base import BaseRoom
from schemas.response.sensor import SensorResponseSchema


# Room Schema
class RoomResponseSchema(BaseRoom):
    id = fields.Integer(required=True)
    sensors = fields.Nested(SensorResponseSchema, many=True)
