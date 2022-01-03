from marshmallow import Schema, fields, validate


class RiddlesCreateRequestSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=255))
    description = fields.String(required=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))
    discount = fields.Float(validate=validate.Range(min=0, max=price))
    number_of_questions = fields.Integer(required=True, validate=validate.Range(min=0))
    questions = fields.String(required=True)
    answers = fields.String(required=True)
