from marshmallow import fields

from schemas.base import BaseSensorStatistic


class SensorStatisticResponseSchema(BaseSensorStatistic):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    timestamp = fields.DateTime(required=True, format="%Y-%m-%dT%H:%M:%S")
