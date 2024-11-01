from marshmallow import fields
from schemas.base import BaseHome


class HomeResponseSchema(BaseHome):
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)