from flasgger import Schema, fields
from marshmallow.validate import Length


class PointPostParamsSchema(Schema):
    lat = fields.Decimal(required=True, example="49.4950")
    lon = fields.Decimal(required=True, example="20.5014")
    datatime = fields.DateTime(required=True, example="2024-05-18 22:35:00")
    route_id = fields.Int(required=True, example="1")


class PointPatchParamsSchema(Schema):
    lat = fields.Decimal(example="49.4950")
    lon = fields.Decimal(example="20.5014")
    datatime = fields.DateTime(example="2024-05-18 22:35:00")
    route_id = fields.Int(example="1")


class PointResponseSchema(Schema):
    id = fields.Int()
    lat = fields.Decimal()
    lon = fields.Decimal()
    datatime = fields.DateTime()
    route_id = fields.Int()

