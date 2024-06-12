from flasgger import Schema, fields
from marshmallow.validate import Length


class RoutePostParamsSchema(Schema):
    name = fields.Str(required=True, validate=Length(min=3, max=50), example="test_user")
    user_id = fields.Int(required=True, example="1")


class RoutePatchParamsSchema(Schema):
    name = fields.Str(validate=Length(min=3, max=50), example="test_user")
    user_id = fields.Int(example="1")


class RouteResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    user_id = fields.Int()


