from marshmallow import Schema, fields


class DiscountIsValidResponseSchema(Schema):
    token = fields.String(required=True)
    questions = fields.String(required=True)
    answers = fields.String(required=True)
    current_question = fields.Integer(required=True)