from marshmallow import fields
from schemas.base import BaseHome
from schemas.response.room import RoomResponseSchema


class HomeResponseSchema(BaseHome):
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
    user_id = fields.Integer(required=True)
    id = fields.Integer(required=True)
    rooms = fields.Nested(RoomResponseSchema, many=True)