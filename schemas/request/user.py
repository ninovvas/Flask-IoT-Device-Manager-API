import re

from marshmallow import (
    Schema,
    fields,
    validate,
    validates,
    validates_schema,
    ValidationError,
)
from marshmallow.validate import OneOf


class UserSchema(Schema):
    username = fields.String(required=True, validate=[validate.Length(min=3)])
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=[validate.Length(min=6)])

    @validates("username")
    def validate_username(self, value):
        if not re.match("^[a-zA-Z0-9_.-]+$", value):
            raise ValidationError(
                "Username can only contain letters, numbers, dots, underscores, and hyphens."
            )

    @validates("password")
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", value):
            raise ValidationError(
                "Password must contain at least one uppercase letter."
            )
        if not re.search(r"[a-z]", value):
            raise ValidationError(
                "Password must contain at least one lowercase letter."
            )
        if not re.search(r"[0-9]", value):
            raise ValidationError("Password must contain at least one number.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValidationError(
                "Password must contain at least one special character."
            )

    @validates("email")
    def validate_email(self, value):
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, value):
            raise ValidationError("Invalid email address format.")


# User Login Schema with custom validation
class UserLoginSchema(Schema):
    username = fields.String(required=False, validate=[validate.Length(min=3)])
    email = fields.Email(required=False)
    password = fields.String(required=True, validate=[validate.Length(min=6)])

    @validates_schema
    def validate_username_or_email(self, data, **kwargs):
        username = data.get("username")
        email = data.get("email")
        if not username and not email:
            raise ValidationError("Either username or email must be provided.")
        if username and email:
            raise ValidationError("Only one of username or email should be provided.")


class UserRegisterSchema(UserSchema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    # role = fields.String(required=True, validate=OneOf(["admin", "user"]))


class UserCreateRequestSchema(UserRegisterSchema):
    role = fields.String(required=True, validate=OneOf(["admin", "user"]))
