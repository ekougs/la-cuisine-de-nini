from marshmallow import Schema
from marshmallow import fields


class DishSchema(Schema):
    name = fields.Str()
    lunch = fields.Bool()
    diner = fields.Bool()


class MenuSchema(Schema):
    complete_dishes = fields.Nested(DishSchema, many=True, allow_none=True)
    main_dishes = fields.Nested(DishSchema, many=True, allow_none=True)
    side_dishes = fields.Nested(DishSchema, many=True, allow_none=True)
