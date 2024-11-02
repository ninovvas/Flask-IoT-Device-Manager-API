from marshmallow import validates, ValidationError

from schemas.base import BaseHome


class HomeRequestSchema(BaseHome):

    @validates("zip_code")
    def validate_zip_code(self, value):
        if len(value) not in (5, 9):
            raise ValidationError("Zip code must be either 5 or 9 digits long.")