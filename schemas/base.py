from marshmallow import Schema, fields


class BaseHome(Schema):
    address = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zip_code = fields.String(required=True)
    user_id = fields.Integer(required=True)