from marshmallow import fields
from schemas.base import BaseRoom

# Room Schema
class RoomRequestSchema(BaseRoom):
    home_id = fields.Integer(required=True)
    id = fields.Integer(required=True)
