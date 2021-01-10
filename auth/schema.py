import re

import phonenumbers
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError, fields, validate, validates

ma = Marshmallow()


class UserSignUpSchema(ma.SQLAlchemySchema):
    username = fields.Str(required=True, validate=validate.Length(max=8))
    email = fields.Str(validate=validate.Email(error="Not a valid email address"))
    password = fields.String(required=True)
    phone_number = fields.String()

    @validates('phone_number')
    def validate_phone_number(self, value):
        try:
            x = phonenumbers.parse(value, "IN")
            if not phonenumbers.is_valid_number(x):
                raise ValidationError("Phone number must be valid and should be of Indian origin.")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("Entry must be a valid phone number")

    @validates('password')
    def validate_password(self, value):
        if not value or len(value) > 6:
            raise ValidationError("Password must not be empty and Password max length allowed is 6.")
        if not re.findall(r'\d', value):
            raise ValidationError("The password must contain at least 1 digit, 0-9.")
        if not re.findall(r'[#_\-]', value):
            raise ValidationError("The password must contain at least 1 symbol: underscore, hyphen or hash")


class UserLogIn(ma.SQLAlchemySchema):
    username = fields.Str(required=True, validate=validate.Length(max=8))
    password = fields.String(required=True)


user_sign_up_schema = UserSignUpSchema()
user_login_schema = UserLogIn()
