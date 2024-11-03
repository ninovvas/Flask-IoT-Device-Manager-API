from marshmallow import fields
from schemas.base import BaseSensorSchedule

class SensorScheduleResponseSchema(BaseSensorSchedule):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)