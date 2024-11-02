from marshmallow import Schema, fields, validate


class BaseHome(Schema):
    address = fields.String(required=True)
    city = fields.String(required=True)
    state = fields.String(required=True)
    zip_code = fields.String(required=True)


class BaseSensor(Schema):
    name = fields.String(required=True, validate=[validate.Length(min=3)])
    sensor_type = fields.String(required=True)
    producer = fields.String(required=True)
    interface = fields.Integer(allow_none=True)

class BaseRoom(Schema):
    name = fields.String(required=True, validate=[validate.Length(min=3)])
    description = fields.String()


