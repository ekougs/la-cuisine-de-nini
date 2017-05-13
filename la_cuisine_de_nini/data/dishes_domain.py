from marshmallow import Schema
from marshmallow import fields


class DishSchema(Schema):
    name = fields.Str()


class TimedDishSchema(Schema):
    lunch = fields.Bool()
    diner = fields.Bool()


class DishesSchema(Schema):
    complete_dishes = fields.Nested(TimedDishSchema, many=True, allow_none=True)
    main_dishes = fields.Nested(TimedDishSchema, many=True, allow_none=True)
    side_dishes = fields.Nested(DishSchema, many=True, allow_none=True)
