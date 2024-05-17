from flasgger import Schema, fields
from marshmallow.validate import Length


class RegistrationSchema(Schema):
    username = fields.Str(required=True, validate=Length(min=3, max=50), example="test_user")
    email = fields.Str(required=True, validate=Length(min=3, max=100), example="test_user@example.com")
    password = fields.Str(required=True, validate=Length(min=3, max=50), example="123456789")


class UserPatchSchema(Schema):
    username = fields.Str(validate=Length(min=3, max=50), example="test_user")
    email = fields.Str(validate=Length(min=3, max=100), example="test_user@example.com")
    password = fields.Str(validate=Length(min=3, max=50), example="123456789")


class UserResponseSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password_hesh = fields.Str()


class LoginSchema(Schema):
    email = fields.Str(required=True, validate=Length(min=3, max=100), example="test_user@example.com")
    password = fields.Str(required=True, validate=Length(min=3, max=50), example="123456789")