from marshmallow import Schema, fields, validate
from marshmallow_enum import EnumField

from models.enums import State


class RiddlesCreateResponseUserSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True, validate=validate.Length(max=255))
    description = fields.String(required=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))
    discount = fields.Float(validate=validate.Range(min=0, max=price))


class RiddlesCreateResponseAdminSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True, validate=validate.Length(max=255))
    description = fields.String(required=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))
    discount = fields.Float(validate=validate.Range(min=0, max=price))
    number_of_questions = fields.Integer(required=True, validate=validate.Range(min=0))
    questions = fields.String(required=True)
    answers = fields.String(required=True)
    status = EnumField(State)
