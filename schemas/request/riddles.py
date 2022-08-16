import required
from marshmallow import Schema, fields, validate
from marshmallow_enum import EnumField

from models import State


class RiddlesCreateRequestSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=255))
    description = fields.String(required=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))
    discount = fields.Float(validate=validate.Range(min=0, max=price))
    number_of_questions = fields.Integer(required=True, validate=validate.Range(min=0))
    questions = fields.String(required=True)
    answers = fields.String(required=True)

    # new fields
    duration = fields.String(required=True)
    where = fields.String(required=True)
    google_map = fields.String(required=True)

    #add hint status_code
    hint = fields.String(required=True)

# class RiddlesEditRequestSchema(RiddlesCreateRequestSchema):
#     status = EnumField(State)
